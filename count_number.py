from ipstw_ku import ipstw as iw
from time import sleep
i = 0
while(True):
  i = i + 1
  if(i>100):
     i = 0
  else:
    iw.oled.fill(0)
    iw.oled.text('Count:  {0:d}'.format(i),0,0)
    iw.oled.show()
    sleep(0.5)
