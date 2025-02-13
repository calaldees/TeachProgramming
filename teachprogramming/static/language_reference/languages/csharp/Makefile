DOCKER_IMAGE:=dotnet
DOCKER_RUN:=docker run --rm -it --volume ${PWD}:/app/:ro -p 5005:5005/udp --volume /app/bin --volume /app/obj ${DOCKER_IMAGE}

compile_and_run_current_folder_in_container:
	${DOCKER_RUN}
build:
	mkdir -p bin obj
	docker build --tag ${DOCKER_IMAGE} .
run:
	docker run --rm -it ${DOCKER_IMAGE}
shell:
	${DOCKER_RUN} /bin/sh
clean:
	rm -rf bin obj
