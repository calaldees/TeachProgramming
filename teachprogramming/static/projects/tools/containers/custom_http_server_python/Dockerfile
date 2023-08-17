FROM python:alpine

WORKDIR /app/

COPY *.py ./

# Alternative
# RUN apk add --no-cache curl
# RUN curl https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/net/http_server.py -O

ENTRYPOINT ["python3", "http_server.py"]
CMD ["./"]
