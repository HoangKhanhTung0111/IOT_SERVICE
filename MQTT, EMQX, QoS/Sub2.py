import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Subscriber2 connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Subscriber2 received: {msg.payload.decode()}")

client = mqtt.Client("subscriber2")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
