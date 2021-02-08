# Variables --------------------------------------------------------------------

PATH_LANGAUGES := languages


# Main -------------------------------------------------------------------------

assert_language_output:
	python3 assert_language_output.py

run_all: python vb php javascript java ruby rust c

language_reference.json: assert_language_output
	python3 language_reference.py


# Languages -------------------------------------------------------------------

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

csharp:
	# https://www.mono-project.com/docs/getting-started/mono-basics/
	# https://kozmicluis.com/compile-c-sharp-command-line/
	# https://stackoverflow.com/questions/8264323/how-to-compile-a-visual-studio-c-sharp-project-with-mono
	cd ${PATH_LANGAUGES}/$@ && \
	msc hello.cs && \
	mono hello.exe

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

mono-csharp:
	# mono-complete  270MB?
	sudo apt-get install mono-mcs -y

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
