#! /usr/bin/python3
# -*- coding: utf8 -*-

from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
import datetime

# la connexion ne sera pas ouverte tout de suite
cluster = Cluster(['localhost', '192.168.0.2'])

# on se connecte. Cela crée un objet session
session = cluster.connect()

session.set_keyspace('passerelles')

query = SimpleStatement(
    """
    INSERT INTO commentaires (article_id, date_commentaire, auteur, contenu)
    VALUES (%(article_id)s, %(date_commentaire)s, %(auteur)s, %(contenu)s)
    """,
    consistency_level=ConsistencyLevel.QUORUM)

session.execute(query, {'article_id': 1, 'date_commentaire': '2021-01-01', 'auteur': "Yacine Charma", 'contenu': "j'aime beaucoup ce livre"})

rows = session.execute('SELECT * FROM commentaires WHERE article_id = 1')
for commentaire in rows:
    print (commentaire.auteur, commentaire.contenu)
