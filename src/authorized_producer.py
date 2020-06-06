import os
from pulsar import Client, AuthenticationToken
from flask import Flask, jsonify, request


# Setup Broker & Topic
broker_url = os.environ.get('BROKER_URL', '')
topic = os.environ.get('TOPIC', '')


# Create Flask app
app = Flask(__name__)


'''
    /message - Publishes provided messages to topic

    Requires Authorization header to be set to communicate with broker
    Forwards string content on provided json body param "message"

    Suggested usage is to provide base64 encoded stringified json
'''
@app.route('/message', methods = ['PUT'])
def produce_message():

    # Setup Pulsar Client
    try:
        token = request.headers['Authorization']
        client = Client(broker_url, authentication=AuthenticationToken(token))
    except Exception as e:
        return 'UNAUTHORIZED'
    
    # Create Producer and send Message
    try:
        producer = client.create_producer(topic)

        payload = request.get_json()
        message = payload['message']
        producer.send(message.encode('utf-8'))
        return 'OK'
    except Exception as e:
        return 'BAD REQUEST'


# If this file is run directly, start the dev server
if __name__ == '__main__': 
    app.run(debug=True, port=8080, host='0.0.0.0')
