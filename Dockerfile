from python:alpine as base

ARG WORKDIR=/teachprogramming
ENV WORKDIR=${WORKDIR}
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}
ENV PYTHONPATH=.


RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing \
&& \
    pip install --upgrade pip \
&& true

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
