FROM python:3

COPY panierachat.py /
COPY exemple.py /

RUN pip install psycopg2-binary

CMD [ "python", "./exemple.py" ]