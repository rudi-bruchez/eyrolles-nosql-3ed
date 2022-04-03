FROM postgres:latest

ENV POSTGRES_USER=app \ 
    POSTGRES_PASSWORD=secret \ 
    POSTGRES_DB=ecommerce

# https://hub.docker.com/_/postgres
COPY commandes.sql /docker-entrypoint-initdb.d/

# CMD [ "psql", "-h localhost", "-U postgres", "-d ecommerce", "-f ./commandes.sql" ]