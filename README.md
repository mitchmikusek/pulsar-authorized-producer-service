# Authorized Producer Service

## Introduuction

This is a simple flask web service that provides an interface to a pulsar producer. The service assumes authorization is requred and expects a `Authorization` header to be set. By sending a `PUT` request to `/message` with a payload of the form
```json
{
    "message":"String Message Here"
}
```
The service will echo the provided message value to the broker on the configured topic. The typical usage pattern consists of a json payload which has been stringified and base64 encoded.

## Setup

You have a couple options to run the app, either dockerized or directly running the source. In either case, the app expects 2 environmental variables to be set, `BROKER_URL` and `TOPIC`. If you are running using the `makefile` commands to launch the service, the docker container will be started with the variables set within the file.

Note that if you run the code directly from source, the server is configured to run on port `8080`, while the docker mapping may differ. For example, if you launch the container using the provided makefile, the variable set for the mapping by defaul is `5000`.

### Docker Setup
Setup and run using provided makefile with variables set in file.
```
    # 0) Ensure Docker is installed and Setup
    # https://docs.docker.com/engine/install/ubuntu/


    # 1) Build Image
    #   docker build --rm -t lottery_publisher:latest .
    make build


    # 2) Run the Image (Attached or Detached)
    # Attached
    #   docker run    --env BROKER_URL=$(BROKER) --env TOPIC=$(TOPIC) -p $(PORT):8080 --name $(APP_NAME) $(APP_NAME)
    make run

    # Detached
    #   docker run -d --env BROKER_URL=$(BROKER) --env TOPIC=$(TOPIC) -p $(PORT):8080 --name $(APP_NAME) $(APP_NAME)
    make run-detached
```

### Run Directly
Setting up and running on the code directly.
```
    # Ensure Python 3.7 is installed

    # Install dependencies
    pip3 install -r requirements.txt

    # Run Dev App
    export BROKER_URL=url_here; export TOPIC=topic; python3 src/authorized_producer.py

    # Run Prod App
    export BROKER_URL=url_here; export TOPIC=topic; python3 src/server.py
```