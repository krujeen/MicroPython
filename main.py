
import BlynkLib
import time 
import network
import urequests
import random
import DFRobot_PH
from umqtt.robust import MQTTClient
from time import sleep
from ipstw_ku import ipstw as iw
from machine import Pin
from machine import ADC

# Config IFTTT
api_key = 'XXXXXXXXXXXXXXXXXXXXXXX'

# Config PIN SENSOR
pin34 = ADC(Pin(34))
pin34.atten(ADC.ATTN_11DB)
pin35 = ADC(Pin(35))
pin35.atten(ADC.ATTN_11DB)

# Connect to WiFi
iw.oled.show_text("WiFi connecting")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("XXXXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXXXX")    
while not wifi.isconnected():       
  time.sleep(0.5)  
iw.oled.text("WiFi connected",0,0)
iw.oled.show()

# Connect to MQTT broker
iw.oled.text("MQTT connecting",0,10)
iw.oled.show()
mqtt = MQTTClient("clientId-XXXXXXXXXXXXXXXXXXXXXXX","broker.mqttdashboard.com")  
mqtt.connect()                                       
iw.oled.text("MQTT connected",0,10)
iw.oled.show()

def sub_cb(topic,msg):             
  if topic == b"krujeen/data/temp": 
    iw.oled.fill(0)             
    iw.oled.text(msg,0,0)       
    iw.oled.show()
mqtt.set_callback(sub_cb)           
mqtt.subscribe("krujeen/data/#")  


# Config BLYNK
BLYNK_AUTH = 'XXXXXXXXXXXXXXXXXXXXXXX'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def on_connect():
  print("connected")
blynk.on_connect(on_connect)

def on_disconnect():
  print("disconnected")
blynk.on_disconnect(on_disconnect)


# User_Task 
def my_user_task():
  temp = pin34.read()
  temp = ((temp * 3.3 / 1024) - 0.5) * 10
  volt = pin35.read()/4095*3.3
  phValue = volt*3.5+2.5
  blynk.virtual_write(1, temp)
  blynk.virtual_write(2, phValue)
  if (phValue >= 8.0) or (phValue <= 5.0) :
    blynk.notify('>>>Alert<<<')

  mqtt_str = "Temperature : "+str(temp)+" PH : "+str(phValue)
  mqtt.check_msg() 
  mqtt.publish("krujeen/data/say",mqtt_str) 
  
  #sensor_readings = {'value1':temp}
  sensor_readings = {'value1':temp, 'value2':phValue}
  request_headers = {'Content-Type': 'application/json'}
  request = urequests.post(
    'http://maker.ifttt.com/trigger/XXXXXXXXXXXXXX/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  print (request.text)
  request.close()
  
blynk.set_user_task(my_user_task, 60000)


# RUN Program
while True :
  blynk.run()
  time.sleep(60)   
