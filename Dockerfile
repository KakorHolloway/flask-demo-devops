FROM harbor.kakor.ovh/public/python:3.9.17

COPY ./app/ /app/

RUN pip install flask sqlalchemy psycopg2
ENV FLASK_APP=/app/app.py 

EXPOSE 5000

CMD flask run --host=0.0.0.0 