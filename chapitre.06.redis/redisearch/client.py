import json 
import urllib.request
from redisearch import Client, IndexDefinition, TextField, NumericField, GeoField, TagField

url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=les-arbres&q=&rows=300"

page = urllib.request.urlopen(url)
if(page.getcode()==200):
    data = page.read()
else:
    print("Error receiving data", page.getcode())

arbres = json.loads(data) 

arbres

exit()

# Creating a client with a given index name
client = Client("ArbresParis")

# # IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix=['nom:', 'espece:', 'genre:', 'hauteur:', 'adresse:', 
    'arrondissement:', 'coordonnées:'])

# # Creating the index definition and schema
client.create_index((TextField("nom", weight=5.0), TagField("espece"), TagField("genre"), 
    NumericField("hauteur"), TextField("adresse"), TextField("arrondissement"), GeoField("coordonnées")), 
    definition=definition)



for a in arbres["records"]:
        print(a)
        print(a["fields"]["libellefrancais"])
        print(a["fields"]["espece"])
        print(a["fields"]["genre"])
        print(a["fields"]["hauteurenm"])
        print(a["fields"]["adresse"])
        print(a["fields"]["arrondissement"])
        print(a["fields"]["geo_point_2d"])
        # print(f'Nom:  {["fields"]["libellefrancais"]} , Espèce : {["fields"]["espece"]}')
  
        # Indexing a document for RediSearch 2.0+
        client.redis.hset(f"arbre:{a[recordid]}",
                        mapping={
                            'nom': a["fields"]["libellefrancais"],
                            'espece': a["fields"]["espece"],
                            'genre': a["fields"]["genre"],
                            'hauteur': a["fields"]["hauteurenm"],
                            'adresse': a["fields"]["adresse"],
                            'arrondissement': a["fields"]["arrondissement"],
                            'coordonnées': a["fields"]["geo_point_2d"]
                        })


# # Simple search
# res = client.search("search engine")

# # Searching with snippets
# res = client.search("search engine", snippet_sizes={"body": 50})

# # Searching with complex parameters:
# q = Query("search engine").verbatim().no_content().with_scores().paging(0, 5)
# res = client.search(q)

# # The result has the total number of results, and a list of documents
# print(res.total)  # "1"
# print(res.docs[0].title)