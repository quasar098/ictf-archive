FROM i386/ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y nmap

WORKDIR /app

COPY persistence /app/persistence
COPY flag.txt /app/flag.txt

RUN chmod -R 555 /app

USER 1000:1000

CMD ncat -vklp 8002 -m 999999 -e /app/persistence