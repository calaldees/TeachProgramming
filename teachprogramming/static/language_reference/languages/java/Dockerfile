FROM eclipse-temurin:25-jdk-alpine
#FROM openjdk:25-jdk-slim
#FROM alpine
#RUN apk add openjdk25-jdk --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

WORKDIR /java
COPY *.java ./
CMD javac *.java && java Java
# docker build --tag java . && docker run --rm -it java