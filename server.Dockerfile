FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt update 
RUN apt install -y iputils-ping iproute2 vim curl
