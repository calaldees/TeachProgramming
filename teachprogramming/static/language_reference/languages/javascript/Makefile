DOCKER_IMAGE:=language_reference_javascript
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
