from redisearch import Client

# Creating a client with a given index name
client = Client("ArbresParis")

res = client.search("@genre:{Ulmus}")

print(res.total)  # "1"
print(res.docs[0].arrondissement)