FROM python:3

LABEL maintainer="koyagabriel@gmail.com"

WORKDIR /var/www

COPY . /var/www

RUN pip install -r requirements.txt