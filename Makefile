PROJECTNAME    = tron
TARGET_VERSION = 1,line,input
help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg & install dependencys/env if needed
	# test          -- run all nosetests
	# blank-db      -- create a blank database
	# run           -- run the site in development mode
	# clean         -- reset the folder to clean git checkout (removes virtual python env)
	# project <PROJECTNAME> <VERSION> -- run the python version of the project (using your system python install, make sure you have pygame installed)

env_activate:
	source env/bin/activate
env_deactivate:
	deactivate

env:
	if dpkg -s python3-setuptools ; then \
	    echo python 3 already installed \
	else \
	    echo installing python 3 \
	    sudo apt-get install python3-setuptools \
	fi
	# Reference - http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/install.html
	virtualenv --no-site-packages -p python3 env
	cd env;	bin/easy_install pyramid

setup: env
	env/bin/python setup.py develop
	#env/bin/populate_MyProject development.ini

run:
	#$(MAKE) env_activate
	env/bin/pserve --reload development.ini
	#$(MAKE) env_deactivate

project:
	cd teachprogramming/static/projects/; ../../../env/bin/python ../../lib/make_ver.py $(PROJECTNAME).py --target_version $(TARGET_VERSION) | python -

clean:
	rm env -rf
	rm *.egg-info -rf
	#rm TeachProgramming.db