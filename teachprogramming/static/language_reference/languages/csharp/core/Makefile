DOCKER_IMAGE:=csharpcore

build:
	docker build --tag ${DOCKER_IMAGE} .
run:
	docker run --rm -it ${DOCKER_IMAGE}
shell:
	docker run --rm -it --volume ${PWD}:/app/ ${DOCKER_IMAGE} /bin/bash