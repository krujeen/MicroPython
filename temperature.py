from ipstw_ku import ipstw as iw
from time import sleep
from machine import Pin
from machine import ADC

pin34 = ADC(Pin(34))
pin34.atten(ADC.ATTN_11DB)
pin35 = ADC(Pin(35))
pin35.atten(ADC.ATTN_11DB)

while True:
  temp = pin34.read()
  temp = ((temp * 3.3 / 1024) - 0.5) * 10
  light = pin35.read()
  iw.oled.fill(0)
  iw.oled.text('TEMP:  {0:.2f}'.format(temp),0,20)
  iw.oled.text('LIGHT:  {0:.2f}'.format(light),0,30)
  iw.oled.show()
  sleep(0.5)
