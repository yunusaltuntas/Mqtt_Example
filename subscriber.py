import paho.mqtt.client as mqtt

broker = "mqtt"
# port
port = 1883
# time to live
time_live = 60


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc), flush=True)
    client.subscribe("/data")


def on_message(client, userdata, msg):
    print(msg.payload.decode(), flush=True)


client = mqtt.Client()
client.connect(broker, port, time_live)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
