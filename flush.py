import redis
import os

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
REDIS_KEY = "words"

print "Clearing old db"
conn.delete(REDIS_KEY)
