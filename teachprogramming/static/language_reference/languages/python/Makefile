DOCKER_IMAGE:=language_reference_python
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run --rm -it ${DOCKER_IMAGE} /bin/sh
