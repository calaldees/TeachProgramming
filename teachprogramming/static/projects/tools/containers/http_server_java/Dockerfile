FROM openjdk:19-alpine

WORKDIR /data/

COPY . .

ENTRYPOINT ["jwebserver", "-b", "0.0.0.0", "-p", "8000", "--directory"]
CMD ["/"]
