DOCKER_IMAGE:=node_test

build:
	docker build --tag ${DOCKER_IMAGE} .

run:
	docker run --rm -it --publish 3000:3000 ${DOCKER_IMAGE}

shell:
	docker run --rm -it --publish 3000:3000 --entrypoint /bin/sh ${DOCKER_IMAGE}