import time
from machine import Pin
from neopixel import NeoPixel

np = NeoPixel (Pin(19),12)
RED = (255,0,0)
YELLOW = (255,150,0)
GREEN = (0,255,0)
CYAN = (0,255,255)
BLUE = (0,0,255)
PURPLE = (180,0,255)

while True :
  np.fill (RED)
  np.write()
  time.sleep(1)
  np.fill(GREEN)
  np.write()
  time.sleep(1)
  np.fill(BLUE)
  np.write()
  time.sleep(1)
  np.fadeinout(PURPLE)
  np.cycle(YELLOW,30)
  np.bounce(CYAN,30)
  np.color_chase(RED,30)
  np.color_chase(YELLOW,30)
  np.color_chase(GREEN,30)
  np.color_chase(CYAN,30)
  np.color_chase(BLUE,30)
  np.color_chase(PURPLE,30)
  np.rainbow_cycle(1)
