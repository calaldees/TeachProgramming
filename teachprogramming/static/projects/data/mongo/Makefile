DOCKER_IMAGE:=pymongo

shell:
	docker run --rm -it \
		--volume ${PWD}:/app/:ro \
		${DOCKER_IMAGE} \
		/bin/bash
build:
	docker build --tag ${DOCKER_IMAGE} .
mongo:
	docker run --rm -it \
		--name mongo \
		--publish 27017:27017 \
		-e MONGO_INITDB_DATABASE="test" \
			mongo

		#-e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
		#-e MONGO_INITDB_ROOT_PASSWORD=secret \

# curl http://host.docker.internal:8000
# client = pymongo.MongoClient("host.docker.internal", 27017)
# https://pypi.org/project/pymongo/