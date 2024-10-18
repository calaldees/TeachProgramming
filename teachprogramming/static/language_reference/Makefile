# Variables --------------------------------------------------------------------

PATH_LANGAUGES := languages


# Main -------------------------------------------------------------------------

build_and_run:
	docker compose up --build

assert_language_output:
	python3 assert_language_output.py

language_reference.json: assert_language_output
	python3 language_reference.py


# Languages -------------------------------------------------------------------

__fake_assert_target:
	# unittest


php:
	cd ${PATH_LANGAUGES}/$@ && \
	php php.php

ruby:
	cd ${PATH_LANGAUGES}/$@ && \
	ruby ruby.rb

rust:
	# TODO



# Clean ------------------------------------------------------------------------

clean:
	# todo