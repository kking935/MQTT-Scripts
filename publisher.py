# python 3.6
import globals
import time
from paho.mqtt import client as mqtt_client

def connect_mqtt():
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

def publish(client):
    msg_count = 0
    while True:
        for topic, msg, callback in globals.srs.topics:
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print("Sending message", msg, "to topic", topic)
            else:
                print("Failed to send message", msg, "to topic", topic)
        msg_count += 1
        time.sleep(15)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
