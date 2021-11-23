DOCKER_IMAGE:=rest_api

build:
	docker build --tag ${DOCKER_IMAGE} .
run:
	docker run --rm -it --publish 8000:8000 ${DOCKER_IMAGE}
shell:
	docker run --rm -it --publish 8000:8000 --volume ${PWD}:/app/:ro ${DOCKER_IMAGE} /bin/sh
