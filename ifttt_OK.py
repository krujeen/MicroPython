import time 
import network
import urequests
import random
from time import sleep
from ipstw_ku import ipstw as iw
from machine import Pin
from machine import ADC

api_key = 'XXXXXXXXXX'
pin34 = ADC(Pin(34))
pin34.atten(ADC.ATTN_11DB)

iw.oled.show_text("WiFi connecting")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Saard_school","XXXXXXXXXX")    
while not wifi.isconnected():       
  time.sleep(0.5)  
iw.oled.show_text("WiFi connected")


while True:    
  temp = pin34.read()
  temp = ((temp * 3.3 / 1024) - 0.5) * 10 
  sensor_readings = {'value1':temp}
  #sensor_readings = {'value1':temp, 'value2':humidity}
  request_headers = {'Content-Type': 'application/json'}
  request = urequests.post(
    'http://maker.ifttt.com/trigger/krujeen_log/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  time.sleep(60) 
