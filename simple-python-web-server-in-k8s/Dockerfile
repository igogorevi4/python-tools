FROM alpine:latest

RUN apk add --no-cache --update python3 curl

WORKDIR /opt/

COPY ./app.py .
RUN chmod +x app.py

ENTRYPOINT ["./app.py"]