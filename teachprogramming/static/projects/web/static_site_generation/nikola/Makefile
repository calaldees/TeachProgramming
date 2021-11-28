DOCKER_IMAGE:=dragas/nikola:alpine
CONTAINER_WORKDIR:=/nikola/
USER=$(shell id -u):$(shell id -g)
DOCKER_RUN_PARMS:=docker run --rm -it --user ${USER} --volume ${PWD}:${CONTAINER_WORKDIR} --publish 8000:8000
DOCKER_RUN:=${DOCKER_RUN_PARMS} --workdir ${CONTAINER_WORKDIR}/demo ${DOCKER_IMAGE}


serve: demo/output
	${DOCKER_RUN} nikola auto --address 0.0.0.0
demo/output: demo
	${DOCKER_RUN} nikola build
demo:
	${DOCKER_RUN_PARMS} --workdir ${CONTAINER_WORKDIR} ${DOCKER_IMAGE} nikola init -q --demo ./demo
shell:
	${DOCKER_RUN} /bin/sh

# see 
#	demo/posts/1.rst
#	demo/pages/listing-demo.rst
