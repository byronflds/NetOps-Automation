import redis
from rq import Queue

redis_conn = redis.Redis(host='localhost', port=6379)

queue = Queue(connection=redis_conn)