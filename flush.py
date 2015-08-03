import redis
import os

redis_key = os.getenv('WORDLIST_KEY', 'words')

conn = redis.Redis(host=os.getenv('REDIS_ENV_TUTUM_SERVICE_HOSTNAME', 'localhost'),
                      port=os.getenv('REDIS_PORT_6379_TCP_PORT', '6379'),
                      password=os.getenv('REDIS_ENV_REDIS_PASS', None))
REDIS_KEY = redis_key

print "Clearing old db"
conn.delete(REDIS_KEY)
