# MicroPython

from ipstw_ku import ipstw as iw
while True:
  while iw.sw1.value()==1:
    pass
  iw.sound(2000,0.5)
  while iw.sw1.value()==0:
    pass
  iw.sound(1000,0.5)
