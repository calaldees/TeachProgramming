DOCKER_IMAGE:=site
DOCKER_RUN:=docker run -it --rm \
	--workdir /app/ \
	--volume ${PWD}:/app/ \
	--volume ${PWD}/../static:/static/ \
	--publish 8000:8000 \
	--env PYTHONPATH=./ \
	${DOCKER_IMAGE}

serve_static: build_static
	open http://localhost:8000/static/
	python3 -m http.server
build_static: build_docker
	${DOCKER_RUN} python3 api.py /static/projects/ /static/language_reference/languages/ --export
build_and_upload: build_static
	scp -r ./api/v1 computingteachers.uk:computingteachers.uk/api
	scp -r ./static computingteachers.uk:computingteachers.uk

run_docker:
	${DOCKER_RUN} python3 api.py /static/projects/ /static/language_reference/languages/
	# -m pdb -c continue
test_docker:
	${DOCKER_RUN} pytest --doctest-modules -s --pdb

build_static_local:
	python3 api.py ../static/projects/ ../static/language_reference/languages/ --export
run_local: static/PatienceDiff.js
	python3 -m pdb -c continue   api.py ../static/projects/ ../static/language_reference/languages/
	# http://localhost:8000/static/index.html
	# http://localhost:8000/api/v1/language_reference.json
test_local:
	PYTHONPATH=./ pytest --doctest-modules

static/PatienceDiff.js:
	cd static ; curl https://raw.githubusercontent.com/jonTrent/PatienceDiff/dev/PatienceDiff.js -O

build_docker:
	docker build --tag ${DOCKER_IMAGE} .
