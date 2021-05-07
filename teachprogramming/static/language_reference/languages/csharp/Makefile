DOCKER_IMAGE:=language_reference_csharp
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run --rm -it ${DOCKER_IMAGE} /bin/bash
