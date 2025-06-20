FROM python:3.11-slim

ENV PYTHONPATH /usr/src/app

WORKDIR /usr/src/app

RUN apt update \
    && apt-get -y install gcc libmariadb-dev \
    && apt install -y default-mysql-client \
    && apt-get install -y default-libmysqlclient-dev \
    && apt install --no-install-recommends -y tzdata \
    && apt-get install -y git \
    && apt clean

COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000
