from datetime import timedelta
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.collection import GetOptions

# cb = couchbase.Couchbase() 
# client = cb.connect("travel-sample", "localhost") 

# res = client.get("21st_amendment_brewery_cafe-north_star_red", quiet=True)
# print(res)


# cluster = Cluster('couchbase://localhost', authenticator=PasswordAuthenticator('dalek', 'Skaro1963'))
cluster = Cluster('couchbase://172.17.0.4', authenticator=PasswordAuthenticator('dalek', 'Skaro1963'))
bucket = cluster.bucket('travel-sample')
coll = bucket.default_collection()
# print (coll)

# opts = GetOptions(timeout=timedelta(seconds=300))
# res = coll.get("airline_1191")
# print (res.content_as[dict], opts)

row_iter = cluster.query('SELECT * FROM `travel-sample` WHERE $1 IN interests', QueryOptions(positional_parameters=['African Swallows']))
for row in row_iter: print(row)