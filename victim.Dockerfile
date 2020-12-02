FROM alpine:latest

WORKDIR /usr/src/app

RUN apk --update --no-cache add curl

# CMD [ "ping","localhost" ]

