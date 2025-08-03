import paho.mqtt.client as mqtt
import time

client = mqtt.Client("publisher")
client.connect("localhost", 1883, 60)

for i in range(5):
    message = f"Hello MQTT #{i}"
    client.publish("test/topic", message)
    print(f"Published: {message}")
    time.sleep(2)

client.disconnect()
