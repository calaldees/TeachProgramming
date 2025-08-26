DOCKER_IMAGE:=fonts

run:
	docker run --publish 8000:8000 --volume ${PWD}/static:/app/static ${DOCKER_IMAGE}

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

animation_base_pygame.py:
	ln -s ../../game/animation_base_pygame.py animation_base_pygame.py
_venv:
	python3 -m venv _venv
	_venv/bin/pip install pygame
run_pygame_font: _venv animation_base_pygame.py
	_venv/bin/python3 font_pygame.py

animation_base.js:
	ln -s ../../game/animation_base.js animation_base.js
http.server: animation_base.js
	python3 -m http.server

font.webp:
	curl https://img.damieng.com/fonts/ch8-previews/Pristine.webp -o font.webp
