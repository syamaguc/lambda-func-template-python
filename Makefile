build:
	docker-compose up --build

test:
	@curl -d '{"name": "syamaguc"}' http://localhost:9000/2015-03-31/functions/function/invocations
