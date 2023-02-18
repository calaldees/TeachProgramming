DOCKER_IMAGE:=wordle
run: build
	docker run --rm --publish 8000:8000 ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell: build
	docker run --rm --publish 8000:8000 -it --entrypoint /bin/sh ${DOCKER_IMAGE}
