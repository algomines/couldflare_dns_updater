# FROM python:3.9-alpine
FROM python:3.8.3-alpine
WORKDIR /apps
COPY code/. /apps/
# RUN yum install python3-pip -y
# RUN yum install libffi-devel python3-devel python-devel -y
# RUN yum install curl -y
# RUN curl -o /tmp/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl
# RUN chmod u+x /var/kubectl/kubectl
RUN pip install --upgrade pip
RUN pip3 install requests
RUN pip3 install subprocess
RUN pip3 install ntplib
# RUN pip3 install websocket-client
# RUN pip3 install rel
# RUN pip3 install termcolor


# RUN python3 ./setup.py install build

# CMD ["/bin/sh", "-c", "python /apps/run.py >> server.log 2>&1"]
CMD ["/bin/sh", "-c", "python /apps/run.py >> /var/logs_op/server.log 2>&1"]