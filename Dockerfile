FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk update
RUN apk -v add make automake gcc g++ subversion python3-dev
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ENV STATIC_PATH /app/app/static


