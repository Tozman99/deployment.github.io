FROM python:alpine


ENV PYTHONUNBUFFERED 1

RUN mkdir /deployment_project

WORKDIR /deployment_project

COPY . /deployment_project

RUN apk update
RUN apk add --virtual deps \
    gcc \
    python-dev \
    linux-headers \
    musl-dev \
    postgresql-dev

RUN apk add --no-cache \
    libpq \
    make

RUN pip3 install -r requirements.txt



