FROM openjdk:21-jdk-slim
WORKDIR /java/
COPY . .
RUN javac Main.java
CMD ["java", "-ea", "Main"]
