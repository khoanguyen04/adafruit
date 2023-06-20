import sys
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = "nttuananh2004"
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("button1")
    client.subscribe("button2")
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint(0,999999)
    client.publish("sensor1", value)
    client.publish("sensor2", value)
    client.publish("sensor3", value)
    time.sleep(5)
    pass