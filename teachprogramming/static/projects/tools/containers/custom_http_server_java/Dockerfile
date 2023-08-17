FROM openjdk:19-alpine

WORKDIR /app/

RUN apk add --no-cache \
    subversion \
&& true
RUN svn export https://github.com/calaldees/javalib/trunk/lib/Utils/Utils

# svn export https://github.com/calaldees/javalib/trunk/lib/Utils
#COPY Utils/ ./
#RUN find ./ -iname *.class -delete

RUN javac Utils/Apps/WebServer.java

RUN find ./ -iname *.java -delete

ENTRYPOINT ["java", "Utils.Apps.WebServer"]
CMD ["./"]