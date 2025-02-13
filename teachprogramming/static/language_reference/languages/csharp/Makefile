DOCKER_IMAGE:=dotnet
DOCKER_RUN:=docker run --rm -it --volume ${PWD}:/app/:ro --volume /app/bin --volume /app/obj

compile_and_run_current_folder_in_container:
	${DOCKER_RUN} ${DOCKER_IMAGE}
build:
	mkdir -p bin obj
	docker build --tag ${DOCKER_IMAGE} .
run:
	docker run --rm -it ${DOCKER_IMAGE}
shell:
	${DOCKER_RUN} --publish 5005:5005/udp ${DOCKER_IMAGE} /bin/sh
clean:
	rm -rf bin obj
