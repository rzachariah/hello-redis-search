import os
from time import time
from redisearch import Client, TextField, IndexDefinition


# Creating a client with a given index name
host = os.getenv("REDIS_HOST")
client = Client("lp-sess-idx", host=host)

SCHEMA = (
    TextField("loc", weight=5.0),
    TextField("lp")
)

# IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix=['lp-sess:'])

try:
    # Get index info. Will throw if index does not exist
    client.info()
except:
    # Create the index
    client.create_index(SCHEMA, definition=definition)

# Create a couple hashes at the zooropa location
client.redis.hset('lp-sess:loc:zooropa:lp:ABC123',
                mapping={
                    'loc': 'zooropa',
                    'lp': 'ABC123',
                    'sess': 'sess1'
                })
client.redis.hset('lp-sess:loc:zooropa:lp:LUPIN',
                mapping={
                    'loc': 'zooropa',
                    'lp': 'LUPIN',
                    'sess': 'sess2'
                })

# Create a couple hashes at the gotham location
client.redis.hset('lp-sess:loc:gotham:lp:BWAYNE',
                mapping={
                    'loc': 'gotham',
                    'lp': 'BWAYNE',
                    'sess': 'sess3'
                })
client.redis.hset('lp-sess:loc:gotham:lp:MATBAN',
                mapping={
                    'loc': 'gotham',
                    'lp': 'MATBAN',
                    'sess': 'sess4'
                })

print("Search by location")
print(client.search(f"@loc:zooropa"))

print("Search by location and exact search on plate")
print(client.search(f"@loc:zooropa@lp:LUPIN"))

print("Search by location and fuzzy search on plate")
print(client.search(f"@loc:zooropa@lp:%LUPAN%"))
