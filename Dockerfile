############################################################
#                   Docker app target                      #
############################################################
FROM python:3.7-alpine AS app

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk update && apk upgrade --no-cache
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt && pip install debugpy
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /volume/data/media
RUN mkdir -p /volume/data/static
RUN adduser -D user
RUN chown -R user:user /volume
RUN chmod -R 755 /volume/data
USER user
