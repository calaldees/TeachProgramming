Practical Containerisation with Docker
======================================

https://gitpod.io#https://github.com/calaldees/dockerWorkshop

Objectives
1. Understand how to practically use Docker though a series of labs
2. Understand some of the theory and technologies behind containerisation

* TASK: Whiteboard
    * What is the difference between virtualisation (virtual machines) and containerisation (virtual environments)?


Hashs
-----

TASK: Describe what a hash is ...

### Hash space

* Orders fo magnitude
    * [How Many Atoms Are There In The World?](https://headsup.scoutlife.org/many-atoms-world/)
        * 10^51
    * [How many electrons are there in the universe?](https://physics.stackexchange.com/questions/174820/how-many-electrons-are-there-in-the-universe)
        * 10^80
* Hash sizes
    * sha-1 == 40 hexadecimal chars == len(str(pow(16,40))) == 10^49 (100 times less atoms than planet earth)
    * sha-256 == 64 hexadecimal chars == len(str(pow(16,64))) == 10^78 (100 times smaller than there are electrons in the universe)
    * sha-512 == 128 hexadecimal chars == len(str(pow(16,128))) == 10^155 (Billions and billions and billions times more elections than the universe)

### Quick `bash` 'poor mans' filehash

TASK: Ues the command below to hash all files in a folder.

```bash
# find the hash of a single file
sha1sum README.md
```

```bash
find /dir1/ -type f -exec sha1sum {} + | sort -k 2 > dir1.txt
cat dir1.txt
sha1sum dir1.txt
```
You've (sort of) created the hash of a overlayfs file layer

Bonus
Recipe for comparing hashs from two directories content
```bash
find /dir1/ -type f -exec sha1sum {} + | sort -k 2 > dir1.txt
find /dir2/ -type f -exec sha1sum {} + | sort -k 2 > dir2.txt
diff -u dir1.txt dir2.txt
```


### Further Reading on Hashs
* [FNV1 in C#](https://github.com/calaldees/TeachProgramming/blob/9f8c68cf787a61b8d210cb88e7c8858326297834/teachprogramming/static/projects/data/hash.ipynb)
* [How SHA-256 Works Step-By-Step](https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/)
* [sha256-animation](https://github.com/in3rsha/sha256-animation) in terminal


OverlayFS Theory
----------------

Visualiser example


First Container
---------------

### First shell

```bash
docker run --rm -it python:alpine /bin/sh
    ls
    echo "hello" > test.txt
    cat test.txt
docker ps -a
    # see no leftover container
    # all state removed `--rm`
```


Getting data/files/state out of a container
-------------------------------------------

### Copy files out of exited container

```bash
docker run -it alpine /bin/sh
    echo "hello" > test.txt
    cat test.txt
    exit
docker ps -a
    # find CONTAINER ID
docker cp 151a6554d794:/test.txt ./
cat test.txt
docker rm 151a6554d794
```

Most of the time we use `--rm` to not track leftover state

### Write to local mounted volume

```bash
docker run --rm -it --volume ${PWD}:/test_mnt/ alpine /bin/sh
    echo "hello2" > /test_mnt/test.txt
cat test.txt
```


Dockerfile (building your own container)
----------

Note for later: Using old `DOCKER_BUILDKIT=0`. Explained later

### First Image

`test.Dockerfile`
```Dockerfile
FROM alpine
RUN echo "hello" > test.txt
```

```bash
docker images
DOCKER_BUILDKIT=0 docker build --file test.Dockerfile --tag test .
docker images
    # see `test`
docker run --rm -it test /bin/sh
    ls 
    # see your test.txt
```


### Debugging building

`test2.Dockerfile`
```Dockerfile
FROM alpine
RUN echo "hello" > test.txt
# deliberately break
RUN exit 1  
RUN echo "hello2" > test.txt
```

Output
```
$ DOCKER_BUILDKIT=0 docker build --file test2.Dockerfile --tag test .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM alpine
 ---> 0ac33e5f5afa
Step 2/4 : RUN echo "hello" > test.txt
 ---> Using cache
 ---> bf3d23693958
Step 3/4 : RUN exit 1
 ---> Running in 9dcbf78c1870
The command '/bin/sh -c exit 1' returned a non-zero code: 1
```

* Every layer you build is cached locally
    * `Step 2/4` --> `Using cache`
    * Developers need to manage this manually! (see alias's later)
* Check the hash's of your layers with the others in your class
    * Same content (should) equal same hash
        * only file content is relevant (file mtime/etc is not part of the hash)

Debug your broken layer
```bash
docker run --rm -it bf3d23693958 /bin/sh
    ls
    cat test.txt
```

### Inspect containers

`test3.Dockerfile`
```Dockerfile
FROM alpine
RUN echo "hello" > test.txt
RUN echo "hello2" > test.txt
```
```bash
DOCKER_BUILDKIT=0 docker build --file test3.Dockerfile --tag test .

docker inspect test
# what do you see?
    # parent, RootFS:layers, architecture, size

docker history --no-trunc test
# what do you see?

# You can enter every previous dockerfile state with the images above
docker run --rm -it ab119c2516bd /bin/sh
```

OverlayFS (Recap)
----------------

Visualiser tree to layers

TASK: What are the advantages and disadvantages of filesystem layering?

<details>

* Great for space - super efficient
* Version control (ish) of files/systems
* Cache needs pruning
* Security?
* Complexity?
</details>

CPU Architectures
-----------------

x86/ARM Magic

My Karaoke system:
* 6 Containers
    * Redis, nginx, postgressql, python, alpine-ffmpeg
* Works on raspberry pi...
    * WHAT?!!! WAIT!!? HOLD UP!?

TASK: Look at `hub.docker.com` search - look at `architecture`
* https://hub.docker.com/search?architecture=arm64&q=&source=verified&type=image
    * ARM, ARM64, x86, x86-64, PowerPC
* ARM
    * https://hub.docker.com/_/nginx
* x86 Only (Wont work with ARM)
    * https://hub.docker.com/r/mwader/static-ffmpeg/tags


Docker BuildKit
---------------

* `DOCKER_BUILDKIT=0 docker <rest of commands>`
    * Old Docker build engine
    * Single process
    * Linear
    * Readable history
* `DOCKER_BUILDKIT=1 docker <rest of commands>`
    * New build engine - parallelisation
    * Hides progress and history
    * Does not expose build layers (where are they kept? they are still on the disk)

* [moby/buildkit: always display image hashes #1053](https://github.com/moby/buildkit/issues/1053)
    * > Yeah, setting DOCKER_BUILDKIT=1 disimproves debug experience a lot. Without DOCKER_BUILDKIT, it was possible to run a container with a layer right before the failed step, and with DOCKER_BUILDKIT it's not possible anymore since it just doesn't show image cached IDs.
        > This looks like a clear regression...

Call me a luddite or old fashioned. BuildKit sucks. 


Multistage builds
-----------------

`multistage_example.Dockerfile`
```Dockerfile
FROM python:alpine as base

WORKDIR /app/

FROM base as download
    # This could install `gcc` or other large compiler tools
    RUN apk add --no-cache \
        curl \
    && true
    # Use the tools to create datafiles - this example just gets some random stuff from the internet
    RUN curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" -O "https://shadedrelief.com/natural3/ne3_data/8192/elev_bump_8k.jpg"
    # These derived files can be copied independently of the tools that built them (curl is not installed in other targets)


FROM base as production
    COPY --from=download /app/ /app/
    CMD ["python3", "-m", "http.server"]
    # Future: Add HEALTHCHECK only for production (see HEALTHCHECK exercise)

# Extension: extra targets
#   this installs some extra dev tools 
FROM base as shell
    COPY --from=download /app/ /app/
    RUN apk add --no-cache \
        bash \
    && true
    CMD ["/bin/bash"]
```

```bash
docker build --file multistage_example.Dockerfile --target production --tag multistage_example .
docker run --rm --publish 8000:8000 multistage_example
    # visit http://localhost:8000/

docker build --file multistage.Dockerfile --target shell --tag multistage_example .
docker run --rm --publish 8000:8000 multistage_example
    # `curl` is not installed
    # but you have all your built files
```

Extension:
* [The smallest Docker image to serve static websites](https://lipanski.com/posts/smallest-docker-image-static-website)
    * `thttpd` 187kb - built with alpine but uses the `scratch` image with no OS installed



Healthcheck
-----------

`healthcheck_example.Dockerfile`
```Dockerfile
FROM python:alpine as base

WORKDIR /app/

RUN apk add --no-cache \
    curl \
&& true

CMD ["python3", "-m", "http.server"]
HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:8000/ || exit 1
```

```bash
docker build --file heathcheck_example.Dockerfile --tag heathcheck_example .
docker run --rm --publish 8000:8000 heathcheck_example
# In another terminal
docker ps -a
    # look at `health`
    # repeat the command and see it over time

docker run --rm -it --publish 8000:8000 heathcheck_example /bin/sh
# In another terminal
docker ps -a
    # look at `health`
# fire up the webserver in the first terminal manually with
    python3 -m http.server
```

* Alternate health checks:
    * `nc -z localhost 8000` check port open
    * `touch -d"-10min" /tmp/marker && [ /processmedia2/data/.heartbeat -nt /tmp/marker ]` file note touched for 10min

We normally only set `HEALTHCHECK`s for production images - they become very annoying in development images


Multi Container Systems
-----------------------

`docker-compose` is a tool (bundled with docker) to orchestrate multiple containers

`database.py`
```python
import mysql.connector

mydb = mysql.connector.connect(
    host="mysql",
    user="test",
    password="test",
    database="test",
)

print(mydb)

# Continue at
# https://www.w3schools.com/python/python_mysql_create_table.asp
# or
# https://realpython.com/python-mysql/
```

`python-mysql.Dockerfile`
```Dockerfile
FROM python:alpine

WORKDIR /app/

RUN apk add --nocache \
    mysql-client \
    mariadb-connector-c \
&& pip install --no-cache-dir \
    mysql-connector-python \
&& true

COPY database.py .
```

`docker-compose.yml`
```yaml
# https://docs.docker.com/compose/compose-file/

services:
    mysql:
        image: mysql
        environment:
            # https://hub.docker.com/_/mysql See Environment Variables
            MYSQL_ROOT_PASSWORD: root
            MYSQL_DATABASE: test
            MYSQL_USER: test
            MYSQL_PASSWORD: test
    python:
        build:
            context: ./
            dockerfile: python-mysql.Dockerfile
        links:
            - mysql
        command: /bin/sh
```

```bash
docker-compose build 
docker-compose run --rm -i python
    # check mysql connects/interacts from the terminal
    mysql --host=mysql --user=test --database=test --password=test
    # play with python
    python database.py
```

### Task
Try a different language or database or both
* [hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)
    * [python_mysql_getstarted](https://www.w3schools.com/python/python_mysql_getstarted.asp)
    * [nodejs_mysql](https://www.w3schools.com/nodejs/nodejs_mysql.asp)
* [hub.docker.com/_/mongo](https://hub.docker.com/_/mongo)
    * [python_mongodb_getstarted](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
    * [nodejs_mongodb](https://www.w3schools.com/nodejs/nodejs_mongodb.asp)
    * [some ideas](https://github.com/calaldees/TeachProgramming/tree/master/teachprogramming/static/projects/data/mongo)

### Alternate/Additional docker-compose files
* docker-compose by default will reference `docker-compose.yml`
* example with other files
    * `docker-compose --file other-docker-compose.yml`  ...
* docker compose files can be combined at runtime
    * `docker-compose --file docker-compose.yml --file docker-compose.more.yml` ...

### Volumes
TODO
```
# volumes:
#    mysql_data:
        # volumes:
        #    - mysql_data:/var/lib/mysql
```



Command Vs Entrypoint (and overriding)
---------------------

`ENTRYPOINT` is another way to launch a container

`entrypoint_example.Dockerfile`
```Dockerfile
FROM alpine
ENTRYPOINT ["ls"]
CMD ["--help"]
```

```bash
docker build --tag entrypoint_example --file entrypoint_example.Dockerfile .
docker run --rm entrypoint_example
docker run --rm entrypoint_example .
docker run --rm entrypoint_example -la

# I want to shell into this container ...
docker run --rm -it entrypoint_example /bin/bash
# Why does this not work? What has happened?
```

```bash
# When an `ENTRYPOINT` is set, all arguments are APPENDED to the entrypoint
# The entrypoint must be overridden explicitly (and MUST be BEFORE the image name `entrypoint_example`)
docker run --rm -it --entrypoint /bin/sh entrypoint_example

# `ENTRYPOINT` can be inspected with
docker inspect entrypoint_example
```



Useful Alias's
--------------

```bash
alias docker_clean='docker volume rm $(docker volume ls -qf dangling=true) ; docker rm $(docker ps -q -f status=exited) ; docker rmi $(docker images -q -f dangling=true)'
alias docker_nuke='docker_rm_all ; docker rmi --force $(docker images -q -a) ; docker volume rm $(docker volume ls -qf dangling=true) ; docker network rm $(docker network ls -q)'
alias docker_ps='docker ps -a --format "{{.ID}}\t{{.Names}}"'
alias docker_rm_all='docker_stop_all ; docker rm $(docker ps -a -q) --force'
alias docker_rm_exited='docker ps -a | grep Exit | cut -d " " -f 1 | xargs docker rm'
alias docker_stop_all='docker stop $(docker ps -a -q)'
```



Why Docker is problematic
----------------

* Docker only allows for composing images by inheriting from a single layer
* All containers run as `root` by default

These are MASSIVE problems - other container technologies solve these problems
dockers prevalence has been seen as 'limiting the progress of better technologies'

Other Container Solutions
-------------------------

* [LXC vs Docker: Which Container Platform Is Right for You? ](https://earthly.dev/blog/lxc-vs-docker/)
    * > Docker used LXC, prior to version 1.0, to create isolation from the host system. Later, Docker developed its own replacement for LXC called libcaontainer. 
    * > Docker containers are made to run a single process per container.
* [LXD](https://linuxcontainers.org/lxd/introduction/)
    * The next generation after `LXC`. Maintains memory state
    * [LXC and LXD: a different container story](https://lwn.net/Articles/907613/)
* [Podman](https://podman.io/)
    * Simply put: `alias docker=podman`
    * Secure by default
    * No Root level daemon
    * [Migrating from Docker to Podman](https://marcusnoble.co.uk/2021-09-01-migrating-from-docker-to-podman/)
* [Singularity](https://sylabs.io/guides/3.5/user-guide/introduction.html)
    * Easily make use of GPUs, high speed networks, parallel filesystems on a cluster or server by default.
    * A simple, effective security model
* [NixOS](https://nixos.org/)
    * > Nix is a tool that takes a unique approach to package management and system configuration. Learn how to make reproducible, declarative and reliable systems. 
    * [Will Nix Overtake Docker?](https://blog.replit.com/nix-vs-docker)
        * repl.it is moving from a single 30gb mega- container to a `nix` package pick and mix approach
        * > Nix takes a first-principles approach to reproducible builds and package management. Nix provides a whole build system that allows for building packages in an isolated way.


Further Reading
---------------

* [Layers between docker builds can't be shared](https://stackoverflow.com/a/60603650/3356840)
    * Sharing docker layers from pulled images is a manual override

Building on CI
* [Docker build cache sharing on multi-hosts with BuildKit and buildx](https://medium.com/titansoft-engineering/docker-build-cache-sharing-on-multi-hosts-with-buildkit-and-buildx-eb8f7005918e)
    * [docker/buildx](https://github.com/docker/buildx)


Unsorted
========

shell == full evaluation - array is not shell

Exec + run
