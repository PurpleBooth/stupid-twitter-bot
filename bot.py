import twitter
import inflect
import os
import time
import redis
from random import shuffle

SECONDS_BETWEEN_TWEETS = 60 * 60
WORDLIST_TXT = "wordlist.txt"
REDIS_KEY = "words"

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
p = inflect.engine()
api = twitter.Api(consumer_key=os.getenv('TWITTER_CONSUMER_KEY', ''),
                  consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET', ''),
                  access_token_key=os.getenv('TWITTER_ACCESS_KEY', ''),
                  access_token_secret=os.getenv('TWITTER_TOKEN_SECRET', ''))

if not conn.exists(REDIS_KEY):
    words = []
    with open(WORDLIST_TXT, "r") as lines:
        for line in lines:
            words.append(line)
    
    shuffle(words)
    
    for word in words:
        print "Appending words " + word
        conn.lpush(REDIS_KEY, word)

print "It's alive!"


def post(word):
    print word
    api.PostUpdate(word)


try:
    while True:
        word = conn.lpop(REDIS_KEY)
        post(word)
        time.sleep(SECONDS_BETWEEN_TWEETS)
except:
    print "Done, bye!"
