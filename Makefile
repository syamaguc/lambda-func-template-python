build:
	@if [ ! -d .env ]; then\
  	echo ".env Directory not exists."; \
		cp -r .env.sample .env; \
	fi
	docker-compose up --build

test-python:
	@curl -d '{"name": "syamaguc"}' http://localhost:9000/2015-03-31/functions/function/invocations

test-node:
	@curl -d '{"name": "syamaguc"}' http://localhost:9090/2015-03-31/functions/function/invocations

update:
	@sls deploy function --function python-app
	@sls deploy function --function node-app
