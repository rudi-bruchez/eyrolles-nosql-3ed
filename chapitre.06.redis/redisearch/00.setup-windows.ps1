# On lance un serveur RediSeach dans Docker
docker pull redislabs/redisearch
docker run -d -p 6379:6379 --name redisearch redislabs/redisearch

# On active un environnement virtuel Python, et j’y télécharge le client officiel RediSearch.
python3 -m venv ./redisearch
.\redisearch\Scripts\activate
pip install redisearch

pip install python-twitter