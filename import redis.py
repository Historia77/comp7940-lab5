import redis

r = redis.Redis(
  host='redis-16043.c1.asia-northeast1-1.gce.cloud.redislabs.com',
  port=16043,
  password='53Fxh6ylJJvRxCRNM1cXyIAp3Ztneho7')

r.ping()

r.set("my_name","zenos")

print(r.get("my_name"))