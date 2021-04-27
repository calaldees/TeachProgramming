build:
	python3 api.py ../static/projects/ ../static/language_reference/languages/ --export

build_and_upload_language_reference: build
	scp ./api/v1/language_reference.json computingteachers.uk:computingteachers.uk/api/v1/

run_local:
	python3 api.py ../static/projects/ ../static/language_reference/languages/
	# http://localhost:8000/static/index.html
	# http://localhost:8000/api/v1/language_reference.json

test:
	PYTHONPATH=./ pytest --doctest-modules
