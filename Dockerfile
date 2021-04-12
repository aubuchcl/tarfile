FROM alpine:latest

RUN apk add --update python3

RUN mkdir -p /opt/package 

WORKDIR /opt/package

COPY ./ ./

COPY ./main.py ./

RUN chmod +x main.py

CMD ./main.py
