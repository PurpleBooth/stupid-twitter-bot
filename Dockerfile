FROM debian:stable

COPY . .

RUN apt-get update && \
    apt-get install -y python-pip && \
    rm -r /var/lib/apt/lists/* && \
    pip install -r requirements.txt && \
    chmod a+x run.sh

ONBUILD COPY wordlist.txt .

CMD run.sh