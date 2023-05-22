# Use the official Python image as a base
FROM python:3.8-slim-buster

RUN apt update && apt install nginx -y

COPY ./nginx/default.conf /ect/nginx/conf.d/default.conf

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app

COPY run.sh .

RUN Chmod +x run.sh

CMD ["./run.sh"]