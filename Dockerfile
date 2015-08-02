FROM debian:stable

COPY . .

RUN apt-get install -y python-pip && \
    pip install -r requirements.txt

ONBUILD COPY wordlist.txt .

CMD python bot.py