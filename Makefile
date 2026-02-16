build_projects_local:
	../language_reference/api.py \
		--path_project teachprogramming/static/projects/ \
 		--path_export  .

deploy: build_projects_local
	rsync \
		api/ \
		margay:~/www/www.computingteachers.uk/api/ \
		-e ssh --archive --verbose --update --inplace --stats --compress
