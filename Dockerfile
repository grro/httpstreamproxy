FROM python:3.9.6-alpine

ENV port 8080
ARG target_url
ARG verify


LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="HttpStreamproxy" \
      org.label-schema.description="A stream proxy" \
      org.label-schema.url="https://github.com/grro/httpstreamproxy" \
      org.label-schema.docker.cmd="docker run -p 8080:8080 -p 8090:8090 grro/proxy"

ADD . /tmp/
WORKDIR /tmp/
RUN  python /tmp/setup.py install
WORKDIR /
RUN rm -r /tmp/

CMD htttpproxy --command listen --port $port --target_url $target_url --verify $verify
