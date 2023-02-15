DOCKER_IMAGE:=image_kernels

run: build
	docker run ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run -it --volume ${PWD}:/java/ ${DOCKER_IMAGE} /bin/sh

run_local:
	reset && javac *.java && java -ea Attempt2

clean:
	find . -name "*.class" -type f -delete