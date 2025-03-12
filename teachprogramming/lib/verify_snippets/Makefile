DOCKER_IMAGE:=language_runner:${language}
DOCKER_RUN:=docker run --rm --workdir /${workdir} --volume ${PWD}/_language_runner:/${workdir}:rw
DOCKER_SHELL:=${DOCKER_RUN} -it ${DOCKER_IMAGE} /bin/sh


test: projects languages
	pytest -s
projects:
	ln -s ../api/v1/projects
languages:
	ln -s ../../static/language_reference/languages

shell:
	# run `pytest --pdb` to failed test
	# language=java workdir=java make shell
	${DOCKER_SHELL}
