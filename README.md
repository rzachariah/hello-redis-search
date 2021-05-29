# hello-redis-search
Playing with RediSearch

## Try it out
docker-compose up --build

```
ranjith.zachariah@Ranjiths-MacBook-Pro hello-redis-search % docker-compose up --build
Building client
Step 1/6 : FROM python:3
 ---> 2a93c239d591
Step 2/6 : WORKDIR /usr/src/app
 ---> Using cache
 ---> 9e16c242e05d
Step 3/6 : COPY requirements.txt ./
 ---> Using cache
 ---> cbb7a5964254
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Using cache
 ---> 2c25b3aa8210
Step 5/6 : COPY . .
 ---> a44bfbbe180c
Step 6/6 : CMD [ "python", "./app.py" ]
 ---> Running in dbdbaea9c882
Removing intermediate container dbdbaea9c882
 ---> e5c3a7a5c6e3

Successfully built e5c3a7a5c6e3
Successfully tagged hello-redis-search_client:latest
Starting hello-redis-search_redis_1 ... done
Recreating hello-redis-search_client_1 ... done
Attaching to hello-redis-search_redis_1, hello-redis-search_client_1
redis_1   | 1:C 29 May 2021 19:21:09.348 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1   | 1:C 29 May 2021 19:21:09.348 # Redis version=6.0.9, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1   | 1:C 29 May 2021 19:21:09.348 # Configuration loaded
redis_1   | 1:M 29 May 2021 19:21:09.350 * Running mode=standalone, port=6379.
redis_1   | 1:M 29 May 2021 19:21:09.351 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1   | 1:M 29 May 2021 19:21:09.351 # Server initialized
redis_1   | 1:M 29 May 2021 19:21:09.355 * <search> Redis version found by RedisSearch : 6.0.9 - oss
redis_1   | 1:M 29 May 2021 19:21:09.355 * <search> RediSearch version 99.99.99 (Git=v1.99.5-184-g72aff0d)
redis_1   | 1:M 29 May 2021 19:21:09.355 * <search> Low level api version 1 initialized successfully
redis_1   | 1:M 29 May 2021 19:21:09.355 * <search> concurrent writes: OFF, gc: ON, prefix min length: 2, prefix max expansions: 200, query timeout (ms): 500, timeout policy: return, cursor read size: 1000, cursor max idle (ms): 300000, max doctable size: 1000000, max number of search results:  1000000, search pool size: 20, index pool size: 8, 
redis_1   | 1:M 29 May 2021 19:21:09.356 * <search> Initialized thread pool!
redis_1   | 1:M 29 May 2021 19:21:09.356 * Module 'search' loaded from /usr/lib/redis/modules/redisearch.so
redis_1   | 1:M 29 May 2021 19:21:09.359 * Loading RDB produced by version 5.0.9
redis_1   | 1:M 29 May 2021 19:21:09.359 * RDB age 606011 seconds
redis_1   | 1:M 29 May 2021 19:21:09.359 * RDB memory usage when created 0.75 Mb
redis_1   | 1:M 29 May 2021 19:21:09.359 # <search> Skip background reindex scan, redis version contains loaded event.
redis_1   | 1:M 29 May 2021 19:21:09.359 * DB loaded from disk: 0.002 seconds
redis_1   | 1:M 29 May 2021 19:21:09.359 * Ready to accept connections
client_1  | Search by location
client_1  | Result{2 total, docs: [Document {'id': 'lp-sess:loc:zooropa:lp:ABC123', 'payload': None, 'loc': 'zooropa', 'lp': 'ABC123', 'sess': 'sess1'}, Document {'id': 'lp-sess:loc:zooropa:lp:LUPIN', 'payload': None, 'loc': 'zooropa', 'lp': 'LUPIN', 'sess': 'sess2'}]}
client_1  | Search by location and exact search on plate
client_1  | Result{1 total, docs: [Document {'id': 'lp-sess:loc:zooropa:lp:LUPIN', 'payload': None, 'loc': 'zooropa', 'lp': 'LUPIN', 'sess': 'sess2'}]}
client_1  | Search by location and fuzzy search on plate
client_1  | Result{1 total, docs: [Document {'id': 'lp-sess:loc:zooropa:lp:LUPIN', 'payload': None, 'loc': 'zooropa', 'lp': 'LUPIN', 'sess': 'sess2'}]}
hello-redis-search_client_1 exited with code 0
```
