DOCKER_IMAGE:=image_kernels

run: build
	docker run ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run -it --volume ${PWD}:/java/ ${DOCKER_IMAGE} /bin/bash

run_local:
	javac *.java && java -ea Main
