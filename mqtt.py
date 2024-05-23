import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, server, port, client_id, username, password):
        self.server = server
        self.port = port
        self.client_id = client_id
        self.username = username
        self.password = password

        self.client = mqtt.Client(client_id=self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code:", rc)

    def on_message(self, client, userdata, message):
        print(f"Received message on topic {message.topic}: {message.payload.decode()}")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection from MQTT Broker!")

    def connect(self):
        # Connect to the MQTT broker
        self.client.connect(self.server, self.port, 60)

    def publish(self, topic, message, qos=0, retain=False):
        # Publish a message to the specified topic
        self.client.publish(topic, message, qos=qos, retain=retain)
        print(f"Message published to topic {topic}: {message}")

    def subscribe(self, topic, qos=0):
        # Subscribe to the specified topic
        self.client.subscribe(topic, qos=qos)
        print(f"Subscribed to topic: {topic}")

    def unsubscribe(self, topic):
        # Unsubscribe from the specified topic
        self.client.unsubscribe(topic)
        print(f"Unsubscribed from topic: {topic}")

    def start(self):
        # Start the MQTT client loop
        self.client.loop_forever()

    def disconnect(self):
        # Disconnect from the MQTT broker
        self.client.disconnect()

# Define the MQTT broker details
MQTT_SERVER = "172.28.182.38"
MQTT_PORT = 1883
CLIENT_ID = "z6a28ihxsodb1hcpi0l4"
USERNAME = "oonp6op4n11e04op59me"
PASSWORD = "6xa2wboijz14ghsdh3lr"

# Create an instance of MQTTClient
mqtt_client = MQTTClient(MQTT_SERVER, MQTT_PORT, CLIENT_ID, USERNAME, PASSWORD)

# Connect to the MQTT broker
mqtt_client.connect()

# Subscribe to a topic
mqtt_client.subscribe("v1/devices/me/telemetry")

# Define a message callback (optional)
def on_message_callback(client, userdata, message):
    print(f"Received message on callback: {message.payload.decode()}")

# Set message callback (optional)
mqtt_client.client.message_callback_add("v1/devices/me/telemetry", on_message_callback)

# Publish a message to a topic
mqtt_client.publish("v1/devices/me/telemetry", "{humid:25}")

# Start the MQTT client loop
mqtt_client.start()

# Disconnect from the MQTT broker (optional)
# mqtt_client.disconnect()
