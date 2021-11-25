DOCKER_IMAGE:=language_reference_csharp
run: build
	docker run --rm -it ${DOCKER_IMAGE}
build:
	docker build --tag ${DOCKER_IMAGE} .
shell:
	docker run \
		--rm -it \
		--volume ${PWD}/csharp.cs:/csharp/csharp.cs:ro \
		${DOCKER_IMAGE} \
		/bin/bash
install_local_dependencies:
	# ubuntu packages
	# mono-vbnc
	sudo apt instal mono-mcs
