import time 
import network
import urequests
from umqtt.robust import MQTTClient
import random
from time import sleep
from ipstw_ku import ipstw as iw
from machine import Pin
from machine import ADC

pin34 = ADC(Pin(34))
pin34.atten(ADC.ATTN_11DB)

iw.oled.show_text("WiFi connecting")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Saard_school","XXXXXXXXXX")    
while not wifi.isconnected():       
  time.sleep(0.5)  
iw.oled.show_text("WiFi connected")

iw.oled.show_text("MQTT connecting")
mqtt = MQTTClient("XXXXXXXXXX","broker.mqttdashboard.com")  
mqtt.connect()                                       
iw.oled.show_text("MQTT connected")

def sub_cb(topic,msg):             
  if topic == b"krujeen/data/temp": 
    iw.oled.fill(0)             
    iw.oled.text(msg,0,0)       
    iw.oled.show()
    
mqtt.set_callback(sub_cb)           
mqtt.subscribe("krujeen/data/#")     
while True:    
  temp = pin34.read()
  temp = ((temp * 3.3 / 1024) - 0.5) * 10 
  temp_str = str(temp)
  mqtt.check_msg() 
  #if iw.sw1.value() == 0:
  mqtt.publish("krujeen/data/say","TEST")  
  urequests.post('http://maker.ifttt.com/trigger/krujeen_log/with/key/XXXXXXXXXX',json={'value1': temp})
  time.sleep(60) 
