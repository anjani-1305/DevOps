FROM ubuntu

RUN apt-get update 
RUN apt-get install python 

RUN pip install flask
RUN pip install flask-mysql

COPY . D:/Kuber/Docker/app.py

ENTRYPOINT FLASK_APP=D:/Kuber/Docker/app.py flask run
