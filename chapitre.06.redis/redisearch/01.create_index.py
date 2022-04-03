from redisearch import Client, IndexDefinition, TextField, NumericField, GeoField, TagField

# Creating a client with a given index name
client = Client("ArbresParis")

# IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix=['arbre:'])

# Creating the index definition and schema
client.create_index((TextField("nom", weight=5.0), TagField("espece"), TagField("genre"), 
    NumericField("hauteur"), TextField("adresse"), TextField("arrondissement"), GeoField("coordonnees")), 
    definition=definition)
