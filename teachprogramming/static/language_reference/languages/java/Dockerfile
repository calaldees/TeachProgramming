#FROM openjdk:17-jdk-alpine
FROM openjdk:22-jdk-slim
WORKDIR /java
COPY *.java ./
CMD javac *.java && java Java
# docker build --tag java . && docker run --rm -it java