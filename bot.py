import twitter
import inflect
import os
import time
import redis
from random import shuffle

SECONDS_BETWEEN_TWEETS = 60 * 60
WORDLIST_TXT = "wordlist.txt"
redis_key = os.getenv('WORDLIST_KEY', 'words')
redis_url = 'redis://' + os.getenv('REDIS_PORT_6379_TCP_ADDR', 'localhost') + ':' + os.getenv(
    'REDIS_PORT_6379_TCP_PORT', '6379')
conn = redis.from_url(redis_url)
p = inflect.engine()
api = twitter.Api(consumer_key=os.getenv('TWITTER_CONSUMER_KEY', ''),
                  consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET', ''),
                  access_token_key=os.getenv('TWITTER_ACCESS_KEY', ''),
                  access_token_secret=os.getenv('TWITTER_TOKEN_SECRET', ''))

if not conn.exists(redis_key):
    words = []
    with open(WORDLIST_TXT, "r") as lines:
        for line in lines:
            words.append(line)

    shuffle(words)

    for word in words:
        print "Appending words " + word
        conn.lpush(redis_key, word)

print "It's alive!"


def post(word):
    print word
    api.PostUpdate(word)


try:
    while True:
        word = conn.lpop(redis_key)
        post(word)
        time.sleep(SECONDS_BETWEEN_TWEETS)
except:
    print "Done, bye!"
