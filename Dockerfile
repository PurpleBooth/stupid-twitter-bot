FROM debian:stable

COPY . .
COPY run.sh .

RUN apt-get update && \
    apt-get install -y python-pip && \
    rm -r /var/lib/apt/lists/* && \
    pip install -r requirements.txt && \
    chmod a+x run.sh flush.sh

ONBUILD COPY wordlist.txt .

ENTRYPOINT /bin/bash run.sh