FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt update 
RUN apt install -y iputils-ping iproute2 curl iptables vim ettercap-text-only
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark

# CMD [ "ping","localhost" ]
