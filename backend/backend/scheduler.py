
from apscheduler.schedulers.background import BackgroundScheduler

import threading
import time
import serial
from xbee import XBee
import paho.mqtt.client as mqtt



from apscheduler.schedulers.background import BackgroundScheduler

import threading
import time
import serial
from xbee import XBee
import paho.mqtt.client as mqtt
from django.utils import timezone
import datetime
from datetime import timedelta 
# Set up the serial port for the XBee module


# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    with open('xbee_data.txt', 'a') as f:
        f.write(msg.payload.decode() + '\n')
        print("Message written to file")

# Subscribe to a topi


def run_scheduler():

    ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)  # Replace with the correct serial port and baud rate for your setup
    # Set up the XBee module
    xbee = XBee(ser, escaped=True)
    # Set up the MQTT client
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883)  # Replace with the address and port of your MQTT broker
    client.subscribe("example/topic")
    client.on_message = on_message
    client.loop_start() 

    for i in range(3):
        try:
            # Wait for a message from the XBee module
            response = xbee.wait_read_frame()
            now = datetime.datetime.now() 
            print(response)
            res_str0 = str(response['frame_id'])
            res_s = res_str0 + str(now)
            client.publish("example/topic", res_s)
        except KeyboardInterrupt:
            break



def run_thread():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scheduler, 'interval', seconds=10)
    scheduler.start()
    while True:
        time.sleep(1)


t = threading.Thread(target=run_thread)
t.start()
