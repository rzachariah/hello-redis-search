import os
from redisearch import Client, TextField, IndexDefinition, Query

# Creating a client with a given index name
host = os.getenv("REDIS_HOST")
client = Client("myIndex", host=host)

SCHEMA = (
    TextField("loc", weight=5.0),
    TextField("lp")
)

# IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix=['lp-sess:'])

# Creating the index definition and schema
client.create_index(SCHEMA, definition=definition)

# Indexing a document for RediSearch 2.0+
client.redis.hset('lp-sess:loc:e9f33a48-4ddd-4c70-a473-8520a1a5cb45:lp:LNL8648',
                mapping={
                    'loc': 'e9f33a484ddd4c70a4738520a1a5cb45',
                    'lp': 'LNL8648'
                })

print(client.redis.hget('lp-sess:loc:e9f33a48-4ddd-4c70-a473-8520a1a5cb45:lp:LNL8648', 'lp'))

# Indexing a document for RediSearch 1.x
client.add_document(
    "lp-sess:loc:e9f33a48-4ddd-4c70-a473-8520a1a5cb45:lp:2NL464",
    loc="e9f33a484ddd4c70a4738520a1a5cb45",
    lp="2NL464",
)

# Simple search
res = client.search("e9f33a484ddd4c70a4738520a1a5cb45")

# the result has the total number of results, and a list of documents
print(res.total) # "2"
print(res.docs[0].lp) # 
print(res.docs[1].lp) # 

# Searching with complex parameters:
# q = Query("search engine").verbatim().no_content().with_scores().paging(0, 5)
# res = client.search(q)
