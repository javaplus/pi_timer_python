import paho.mqtt.client as mqtt
import json
import logging
import sys
import timer
import math
import os


serverIP = os.environ['pi_server_ip']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("timer/timer")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    jsonRequest = json.loads(msg.payload)
    timeToEnd = jsonRequest['timeToEnd']
    speaktime = jsonRequest['speaktime']
    speakinterval = jsonRequest['speakinterval']
    timer.stopCountDown()
    timeToEndLong = float(timeToEnd)   
    timeToEndInt = int(math.floor(timeToEndLong))
    timer.countDown(timeToEndInt, speaktime,speakinterval)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(serverIP, 1883, 60)
#client.connect("192.168.1.112", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
