FROM python:3-alpine

ENV port 80
ENV target_url ?
ENV verify ?


RUN cd /etc
RUN mkdir app
WORKDIR /etc/app
ADD *.py /etc/app/
ADD requirements.txt /etc/app/.
RUN pip install -r requirements.txt

CMD python /etc/app/httpproxy.py $port $target_url $verify



