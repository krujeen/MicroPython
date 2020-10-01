########## sw1-1.py ###########
from time import sleep
from ipstw_ku import ipstw as iw
while True:
    if iw.sw1.value() == 0:
      print("Switch is pressed")
    else:
      print("Switch is released")
    sleep(0.5)


########## sw1-2.py ###########
from time import sleep
from ipstw_ku import ipstw as iw
while True:
    if iw.sw1.value() == 0:
      iw.led.value(1)
    else:
      iw.led.value(0)


######## sw1-3.py ###########
from time import sleep
from ipstw_ku import ipstw as iw
while True:
    while iw.sw1.value() == 1:
      pass
    while iw.sw1.value() == 0:
      pass
    if iw.led.value() == 1:
      iw.led.value(0)
    else:
      iw.led.value(1)
