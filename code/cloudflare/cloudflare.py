
import requests,subprocess,time,ntplib,logging,base64
# logging.basicConfig( encoding='utf-8', level=logging.DEBUG)
class dns():
    endpoint = 'https://api.cloudflare.com/client/v4/'
    requestDelayInSeconds = 3
    publicIP=''
    def __init__(self, ACCOUNT_ID='', ZONE_IDENTIFIER='',DNS_TOKEN='', **kwargs):
        self.account_id=base64.b64decode(ACCOUNT_ID).decode('utf-8')
        self.zone_identifier=base64.b64decode(ZONE_IDENTIFIER).decode('utf-8')
        self.token=base64.b64decode(DNS_TOKEN).decode('utf-8')
        self.session = requests.Session()
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Authorization': 'Bearer {token}'.format(token=self.token),
                }
        self.session.headers.update(self.headers)

    def chkNet(self):
        try:
            client = ntplib.NTPClient()
            client.request('pool.ntp.org')
            return True
        except OSError:
            return False

    def rGet(self,path,headers={},data={}):
        if len(headers)>0:
            self.session.headers.update(headers)
        return self.session.get(url = self.endpoint+path, params = data)
        
    def chkToken(self):
        response = self.rGet('user/tokens/verify')
        if response.status_code==200:
            response = response.json()
            return True if response["success"] is True else False
        elif response.status_code != 401:
            time.sleep(self.requestDelayInSeconds)
            return self.chkToken()
        else:
            return False
    
    def getCluserDomains(self):
        a = subprocess.run(["/var/kubectl/kubectl", "get", "ing", "-A", "-o=jsonpath='{.items..spec..host}'"],shell=True, check=True, capture_output=True, text=True)
        return a.stdout.replace("'", "").split(' ')

    def listDNZRecords(self):
        response = self.rGet('zones/{zone_identifier}/dns_records'.format(zone_identifier=self.zone_identifier))
        if response.status_code==200:
            response = response.json()
            return response['result'] if response["success"] is True else []
        elif self.chkToken() is True:
            time.sleep(self.requestDelayInSeconds)
            return self.listDNZRecords()
        else:
            return []

    def getClusterPublicIP(self):
        x = requests.get('https://ipinfo.io/json')
        if x.status_code==200:
            x = x.json()
            return x["ip"]
        else:
            time.sleep(self.requestDelayInSeconds)
            return self.getClusterPublicIP()

    def getClusterPublicIPv6(self):
        x = requests.get('https://api64.ipify.org?format=json')
        if x.status_code==200:
            x = x.json()
            return x["ip"]
        else:
            time.sleep(self.requestDelayInSeconds)
            return self.getClusterPublicIP()

    def getPointingRecords(self,domains=[],filter=False):
        r = self.listDNZRecords()
        rx = []
        for a in r:
            if a['type'] == 'A' or  a['type'] == 'AAAA':
                if a['name'] in domains or filter is False:
                    rx.append(a)
        return rx

    def sycIP2DNS(self):
        status = []
        logging.info('Checking IP Address')
        publicIP = self.getClusterPublicIP()
        publicIPv6 = self.getClusterPublicIPv6()
        if self.publicIP != publicIP:
            self.publicIP = publicIP
            logging.warning('New IPv4: {message}'.format(message=publicIP))
            logging.warning('New IPv6: {message}'.format(message=publicIPv6))
            records = self.getPointingRecords(domains=self.getCluserDomains(),filter=True)
            for x in records:
                if (x['type'] == 'A' and x['content']!=publicIP) or (x['type'] == 'AAAA' and x['content']!=publicIPv6):
                    ip = publicIP if (x['type'] == 'A' and x['content']!=publicIP) else publicIPv6
                    url = self.endpoint+'zones/{zone_identifier}/dns_records/{identifier}'.format(zone_identifier=self.zone_identifier,identifier=x['id'])
                    data = {'content': ip}
                    response = self.session.patch(url = url, json=data)
                    if response.status_code==200:
                        response = response.json()
                        if response["success"] is True:
                            logging.warning('{name}: IPv{type}->{message}'.format(name=x['name'],type='4' if (x['type'] == 'A' and x['content']!=publicIP) else '6',message=ip))
                            status.append({'name':x['name'],'ip':ip,'response':response})
                    elif response.status_code != 401:
                        time.sleep(self.requestDelayInSeconds)
                        rb = self.sycIP2DNS()
                        if rb is not False:
                            for d in rb:
                                status.append(rb[d])
                            return status
                        else:
                            self.publicIP = ''
                            return False
                    else:
                        self.publicIP = ''
                        return False
        return status