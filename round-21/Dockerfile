FROM ubuntu AS builder
RUN apt update -y && apt install -y clangd
RUN mkdir /app && ln -s `which clangd` /app/run

FROM redpwn/jail

COPY --from=builder / /srv
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 744 /srv/app/flag.txt

ENV JAIL_TIME 60
ENV JAIL_CONNS_PER_IP 1
ENV JAIL_MEM 20M
