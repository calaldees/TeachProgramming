DOCKER_IMAGE:=wordle
run: build
	docker run --rm --publish 8000:8000 ${DOCKER_IMAGE}
build: words
	docker build --tag ${DOCKER_IMAGE} .
shell: build
	docker run --rm --publish 8000:8000 -it --entrypoint /bin/sh ${DOCKER_IMAGE}

words:
	curl -s https://raw.githubusercontent.com/tabatkins/wordle-list/main/words -O
