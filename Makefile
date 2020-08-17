#CI_COMMIT_REF_NAME   ?= $(shell git symbolic-ref --short -q HEAD)
#CI_COMMIT_SHORT_SHA  ?= $(shell git rev-parse HEAD | cut -c 1-8)

DOCKER_IMAGE:=teachprogramming:latest

build:
	docker build \
		--tag ${DOCKER_IMAGE} \
	.

.PHONY: example
example:
	python3 teachprogramming/lib/make_ver.py teachprogramming/static/projects/game/tron.py --ver_name base4
	python3 teachprogramming/lib/make_ver.py teachprogramming/static/projects/game/tron.py --ver_name base4 --ver_prev base3