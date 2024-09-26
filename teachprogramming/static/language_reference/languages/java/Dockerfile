#FROM openjdk:17-jdk-alpine
#FROM eclipse-temurin:23-jdk-alpine
FROM openjdk:24-jdk-slim
WORKDIR /java
COPY *.java ./
CMD javac *.java && java Java
# docker build --tag java . && docker run --rm -it java