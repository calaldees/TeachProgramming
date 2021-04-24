DOCKER_IMAGE:=language_reference_java
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
