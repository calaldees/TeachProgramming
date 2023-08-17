Container Workshop (1 hour)
==================

Prerequisites
-------------

* `docker build`
* `docker run --rm -it`
* `docker ps -a`
* `docker rm xxxxx`


Workshop
--------

1. Run a container in one of the folders
    * `make build`
    * `make run`
    * `localhost:8000`
    * Q: What is this container doing?
2. Look at the `Makefile`
    * Q: what is does `make` do?
3. Look at a `Dockerfile` in two of the folders
    * Q: what are some of the core keywords? What do these keywords they do?
4. Run another container in another one of the folders
    * Q: What is the difference between them (e.g. `http_server_python` and `custom_http_server_python`)
5. run `make run_volume`
    * create any text file (maybe called `test.txt`)
    * Q: What is volume?
    * Q: What is the difference between a file in an `image` and a file in a `volume`?
6. Pair - investigate the code of `http_server.py`
    * Try to describe what any of the lines might be doing using technical terminology
    * Write down the technical terms - consolidate as group
7. Look at `docker-compose.yml`
    * Q: What is this file doing?
8. Run `docker-compose up`
    * visit `:8001` `:8002` `:8003` `:8004`
    * Look at the terminal log
    * Q: What is `docker-compose`?
9. Why would we ever use

Group:
* Verbally describe each of the questions above to the group
* I will ask these exact questions as a starter for next session


Unsorted
========

<details>
<summary>unused old notes</summary>


```bash
docker build --tag http_server_python .
docker images
docker run --rm -it http_server_python /bin/sh
curl https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/net/http_server.py -O
# Native python (NOT IN CONTAINER!)
python3 http_server.py
# Explore public browser
    FROM python:alpine
    WORKDIR /app/
    COPY *.py ./
    ENTRYPOINT ["http_server.py"]  #DELIBERATE!
docker run --rm -it --entrypoint /bin/sh http_server_python
# rebuild?
8000 not served?
docker run --rm -it --publish 8000:8000 http_server_python

openjdk:19-alpine
jwebserver -b 0.0.0.0 -p 8000
https://openjdk.java.net/jeps/408

Makefile
help/build/run

git status
.gitignore
```

</details>