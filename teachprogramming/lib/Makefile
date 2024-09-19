DOCKER_IMAGE:=site
DOCKER_RUN:=docker run -it --workdir /app/ --volume ${PWD}:/app/ --volume ${PWD}/../static:/static/ --publish 8000:8000 ${DOCKER_IMAGE}

run_local: static/PatienceDiff.js
	python3 -m pdb -c continue   api.py ../static/projects/ ../static/language_reference/languages/
	# http://localhost:8000/static/index.html
	# http://localhost:8000/api/v1/language_reference.json
run_docker: 
	${DOCKER_RUN} python3 -m pdb -c continue api.py /static/projects/ /static/language_reference/languages/

build_local:
	python3 api.py ../static/projects/ ../static/language_reference/languages/ --export
build: docker
	${DOCKER_RUN} python3 api.py /static/projects/ /static/language_reference/languages/ --export
build_and_upload: build
	scp -r ./api/v1 computingteachers.uk:computingteachers.uk/api
	scp -r ./static computingteachers.uk:computingteachers.uk

static/PatienceDiff.js:
	cd static ; curl https://raw.githubusercontent.com/jonTrent/PatienceDiff/dev/PatienceDiff.js -O

test:
	PYTHONPATH=./ pytest --doctest-modules

docker:
	docker build --tag ${DOCKER_IMAGE} .
