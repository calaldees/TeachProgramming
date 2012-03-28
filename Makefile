
help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg
	# test          -- run all nosetests
	# blank-db      -- create a blank database
	# run           -- run the site in development mode
	# clean         -- reset the folder to clean git checkout

setup-env:
	# Reference - http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/install.html
	#sudo apt-get install python3-setuptools
	#sudo easy_install virtualenv
	virtualenv --no-site-packages env
	cd env
	bin/easy_install pyramid

env_activate:
	source env/bin/activate
env_deactivate:
	deactivate

setup-project: setup-env
	#$(MAKE) env_activate
	env/bin/python setup.py develop
	#populate_MyProject development.ini
	#$(MAKE) env_deactivate

setup: setup-env setup-project

run:
	#$(MAKE) env_activate
	env/bin/pserve --reload development.ini
	#$(MAKE) env_deactivate
