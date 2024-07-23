
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
b = r.set('foo', 'bar')
print("set: " + str(b))
v = r.get('foo')
print("value: " + v)
print("OK")
