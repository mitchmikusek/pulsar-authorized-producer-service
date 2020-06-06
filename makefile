APP_NAME=lottery_publisher
PORT=5000
BROKER=pulsar://panel.moonmoon.live:6650
TOPIC=non-persistent://moonmoon/lottery/drawings

.PHONY: build run stop list clean list-containers list-images

build:
	docker build --rm -t $(APP_NAME):latest .

run:
	docker run    --env broker_url=$(BROKER) --env topic=$(TOPIC) -p $(PORT):8080 --name $(APP_NAME) $(APP_NAME)

run-detached:
	docker run -d --env broker_url=$(BROKER) --env topic=$(TOPIC) -p $(PORT):8080 --name $(APP_NAME) $(APP_NAME)

attach:
	docker attach $(APP_NAME)

stop:
	docker stop $(APP_NAME)

list-containers:
	docker container list

list-images:
	docker image ls

clean:
	docker system prune -af