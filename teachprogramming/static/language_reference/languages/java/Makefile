DOCKER_IMAGE:=language_reference_java
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
run_local:
	javac *.java && java Java