FROM debian:11.1

RUN apt-get update && apt-get -y install \
        ca-certificates \
        librdkafka++1 \
        librdkafka-dev \
        librdkafka1 \
        python3 \
        python3-pip \
        && apt-get clean all

COPY kafka/requirements.txt .

RUN pip3 install -r requirements.txt
