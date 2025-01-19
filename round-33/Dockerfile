FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev ncat

WORKDIR /app

COPY . /app

RUN chmod -R 555 /app
RUN chmod 777 /app/db.db

USER 1000:1000

CMD ncat -klvp 12002 -m 999999 -e ./wrapper.sh