FROM debian:stable

COPY . .

RUN apt-get update && \
    apt-get install -y python-pip && \
    rm -r /var/lib/apt/lists/* && \
    pip install -r requirements.txt

ONBUILD COPY wordlist.txt .

CMD python bot.py