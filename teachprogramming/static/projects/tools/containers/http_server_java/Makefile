DOCKER_IMAGE:=http_server_java

help:
	# This is some help

build:
	docker build --tag ${DOCKER_IMAGE} .

run:
	docker run --rm -it --publish 8000:8000 ${DOCKER_IMAGE}

run_volume:
	docker run --rm -it --publish 8000:8000 --volume ${PWD}:/data/ ${DOCKER_IMAGE} /data/

shell:
	docker run --rm -it --publish 8000:8000  ${DOCKER_IMAGE} /bin/sh