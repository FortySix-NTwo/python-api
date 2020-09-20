############################################################
#                   Docker app target                      #
############################################################
FROM python:3.7-alpine AS app

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk update && apk upgrade --no-cache
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt && pip install debugpy
RUN apk del .tmp-build-deps

RUN mkdir /app

WORKDIR /app

COPY ./app /app

RUN adduser -D user
USER user
