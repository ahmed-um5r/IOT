import paho.mqtt.client as mqtt
import serial
from xbee import XBee
from django.utils import timezone
import datetime
from datetime import timedelta
import time
# Set up the serial port for the XBee module
ser = serial.Serial('COM1', 9600)  # Replace with the correct serial port and baud rate for your setup

# Set up the XBee module
xbee = XBee(ser, escaped=True)

# Set up the MQTT client
client = mqtt.Client()
client.connect("127.0.0.1", 1883)  # Replace with the address and port of your MQTT broker

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    with open('xbee_data.txt', 'a') as f:
        f.write(msg.payload.decode() + '\n')
        print("Message written to file")

# Subscribe to a topic
client.subscribe("example/topic")

# Set the callback function for incoming messages
client.on_message = on_message

# Start the MQTT loop
client.loop_start()

# Wait for incoming messages
while True:
    try:
        # Wait for a message from the XBee module
        response = xbee.wait_read_frame()
        now = datetime.datetime.now()
        # Convert the payload to a string
#        payload ="D0"       
        # Publish the payload to the MQTT broker
        console.log(response)
        res_str0=str(response['frame_id'])
        res_s=res_str0+str(now)
        client.publish("example/topic", res_s)
    except KeyboardInterrupt:
        break

# Stop the MQTT loop
client.loop_stop()