import paho.mqtt.client as mqtt
import os

serverIP = os.environ['pi_server_ip']

def broadcastEvent(eventName):
    mqttc = mqtt.Client("globalEventEmmitter")
    mqttc.connect(serverIP, 1883)
    # don't retain messages, this needs to be more real -time
    mqttc.publish("events/global", payload=str(eventName),qos=0,retain=False) 
    mqttc.loop(2) #timeout = 2s

