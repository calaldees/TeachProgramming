# Variables --------------------------------------------------------------------

PATH_LANGAUGES := languages


# Main -------------------------------------------------------------------------

assert_language_output:
	python3 assert_language_output.py

run_all: python vb php javascript java ruby rust c

language_reference.json: assert_language_output
	python3 language_reference.py


# Langauages -------------------------------------------------------------------

__fake_assert_target:
	# unittest

javascript:  # requires spidermonkey
	cd ${PATH_LANGAUGES}/$@ && \
	js javascript.js

python:
	cd ${PATH_LANGAUGES}/$@ && \
	python3 python.py

java:
	cd ${PATH_LANGAUGES}/$@ && \
	javac Java.java && \
	java Java

vb:
	cd ${PATH_LANGAUGES}/$@ && \
	vbnc vb.vb && \
	mono vb.exe

php:
	cd ${PATH_LANGAUGES}/$@ && \
	php php.php

ruby:
	cd ${PATH_LANGAUGES}/$@ && \
	ruby ruby.rb

rust:
	# TODO

c:
	cd ${PATH_LANGAUGES}/$@ && \
	gcc -Wall c.c -o c
	./c


# Install Languages ------------------------------------------------------------

mono-basic:
	git clone git@github.com:mono/mono-basic.git
	cd mono-basic
	./configure
	make && sudo make install

install:
	brew install mono spidermonkey


# Clean ------------------------------------------------------------------------

clean:
	rm *.class
	rm *.exe
	rm *.pyc
