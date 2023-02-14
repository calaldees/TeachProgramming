#FROM openjdk:21-jdk-slim
# https://developers.redhat.com/articles/2022/09/16/updating-docker-hubs-openjdk-image#eclipse_adoptium_builds_jdks
# https://en.wikipedia.org/wiki/Java_version_history
# https://docs.oracle.com/en/java/javase/
FROM eclipse-temurin:19-jdk-alpine
WORKDIR /java/
COPY . .
RUN javac Main.java
CMD ["java", "-ea", "Main"]
