FROM python:latest

WORKDIR /app

COPY producer.py .
COPY consumer.py .

RUN pip install kafka-python influxdb