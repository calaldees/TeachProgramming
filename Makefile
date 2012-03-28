
help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg
	# test          -- run all nosetests
	# blank-db      -- create a blank database
	# run           -- run the site in development mode
	# clean         -- reset the folder to clean git checkout

env_activate:
	source env/bin/activate
env_deactivate:
	deactivate

env:
	# Reference - http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/install.html
	#sudo apt-get install python3-setuptools
	virtualenv --no-site-packages -p python3 env
	cd env;	bin/easy_install pyramid

setup: env
	env/bin/python setup.py develop
	#env/bin/populate_MyProject development.ini


run:
	#$(MAKE) env_activate
	env/bin/pserve --reload development.ini
	#$(MAKE) env_deactivate
