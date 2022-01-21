FROM alpine

RUN apk add --no-cache \
    gcc \
    libc-dev


WORKDIR /c
COPY *.c ./
CMD gcc -Wall c.c -o c && ./c
