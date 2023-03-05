FROM python:3.10-alpine

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV HOST 0.0.0.0
EXPOSE 8010

COPY . .
