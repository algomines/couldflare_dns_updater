from cloudflare import dns as cfDNS
from envVARs import get as envVarsGet
import time, logging
sleep_time = 5
envVars = envVarsGet(ACCOUNT_ID='e5c75d8176bc01607b6fa1474bba3d00', ZONE_IDENTIFIER='d7b56e70bb53e20f929c4b39878ec16f',DNS_TOKEN='kohx2t4tWFInDCsJGtzCNC444UI8zqcRmc10AJLW')
cfDNS = cfDNS(**envVars)
net=False
while True:
    # try:
    #     iNet = cfDNS.chkNet()
    #     if iNet!=net:
    #         net=iNet
    #         logging.warning('Connection: {message}'.format(message='OK' if net else 'LOST'))
    #         if net:
    #             cfDNS.sycIP2DNS()
    # except Exception as e:
    #     net= None
    #     logging.warning('Loop Info: {message}'.format(message=e))
    time.sleep(sleep_time)