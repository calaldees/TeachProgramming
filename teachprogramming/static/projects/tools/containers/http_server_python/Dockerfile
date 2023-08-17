FROM python:alpine

WORKDIR /data/

COPY . .

ENTRYPOINT ["python3", "-m", "http.server", "-b", "0.0.0.0", "--directory"]
CMD ["./"]