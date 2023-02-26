import paho.mqtt.client as mqtt
import serial

# Connect to the serial port of the XBee module
ser = serial.Serial('COM9', 9600)

# Define the MQTT client and connect to the broker
client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

# Define the callback function to be executed when a message is received
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))

# Set the callback function to be executed when a message is received
client.on_message = on_message

# Subscribe to the topic where messages will be received
client.subscribe("xbee/commands")

# Loop to continuously read data from the XCTU console and publish it to the broker
while True:
    data = input("Enter message: ")
    ser.write(bytes(data + '\r\n', 'utf-8'))
    client.publish("xbee/data", data)

# Disconnect from the broker and close the serial connection
client.disconnect()
ser.close()
