#!/usr/bin/python3
import requests
import json
import redis

url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=fontaines-a-boire&q=&facet=type_objet&facet=modele&facet=commune&facet=dispo"

r = redis.Redis(host='localhost', port=6379, db=0)

fontaines = json.loads(requests.get(url).content.decode('utf-8'))

for fontaine in fontaines["records"]:
    d = fontaine["fields"]
    del d["geo_shape"]
    del d["geo_point_2d"]
    r.hset(fontaine["fields"]["gid"], mapping=d)