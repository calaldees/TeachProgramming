DOCKER_IMAGE:=fonts

run:
	docker run --publish 8000:8000 ${DOCKER_IMAGE}

build:
	docker build --tag ${DOCKER_IMAGE} .

shell:
	docker run \
		--publish 8000:8000 \
		-it \
		--rm  \
		--volume "${PWD}:/app" \
		-u $(id -u):$(id -g) \
		${DOCKER_IMAGE} \
			/bin/sh

font.png:
	curl https://images.damieng.com/fonts/zx-origins/Prince.png -o font.png
