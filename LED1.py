########## LED1.py ################
from time import sleep
from ipstw_ku import ipstw as iw
while True:
  iw.led.value(0)
  sleep(1)
  iw.led.value(1)
  sleep(1)


########## LED2.py ################
from time import sleep
from ipstw_ku import ipstw as iw
while True:
  led.value(0)
  sleep(0.1)
  led.value(1)
  sleep(0.1)


########## LED3.py ################
from time import sleep
from ipstw_ku import ipstw as iw
while True:
  led.value(0)
  sleep(1)
  led.value(1)
  sleep(0.05)


########## LED4.py ################
from time import sleep
from ipstw_ku import ipstw as iw
from machine import Pin
led = Pin(19,Pin.OUT)
while True:
  led.value(0)
  sleep(1)
  led.value(1)
  sleep(1)
