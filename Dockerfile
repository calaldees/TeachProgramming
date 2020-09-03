FROM python:alpine

ENV WORKDIR=/teachprogramming/
WORKDIR ${WORKDIR}

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

