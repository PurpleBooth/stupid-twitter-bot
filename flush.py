import redis
import os

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_key = os.getenv('WORDLIST_KEY', 'words')

conn = redis.from_url(redis_url)
REDIS_KEY = redis_key

print "Clearing old db"
conn.delete(REDIS_KEY)
