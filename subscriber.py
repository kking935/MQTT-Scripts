# python3.6
import globals
from paho.mqtt import client as mqtt_client

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(globals.client_id)
    client.username_pw_set(globals.username, globals.password)
    client.on_connect = on_connect
    client.connect(globals.broker, globals.port)
    return client

def subscribe(client: mqtt_client, topics: any):
    def on_message(client, userdata, msg):
        print("New message received: ", msg.payload.decode())

    for topic, msg, callback in topics:
        client.subscribe(topic)
        client.message_callback_add(topic, callback)

    client.on_message = on_message

def run(topics):
    client = connect_mqtt()
    subscribe(client, topics)
    client.loop_forever()

if __name__ == '__main__':
    run()
