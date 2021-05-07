DOCKER_IMAGE:=language_reference_vb
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run \
		--rm -it \
		--volume ${PWD}/vb.vb:/vb/vb.vb:ro \
		${DOCKER_IMAGE} \
		/bin/bash
