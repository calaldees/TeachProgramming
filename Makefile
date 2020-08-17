#CI_COMMIT_REF_NAME   ?= $(shell git symbolic-ref --short -q HEAD)
#CI_COMMIT_SHORT_SHA  ?= $(shell git rev-parse HEAD | cut -c 1-8)

DOCKER_IMAGE:=teachprogramming:latest

build:
	docker build \
		--tag ${DOCKER_IMAGE} \
	.
