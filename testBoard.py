from time import sleep
from ipstw_ku import ipstw as iw
from math import sin,cos,radians
import umpush8pt,umpush10pt,umpush12pt

def test_oled():
  iw.oled.set_font()
  iw.oled.show_text("OLED test start")
  sleep(1)
  iw.oled.fill(0)
  iw.oled.text("Line 1",0,0)
  iw.oled.show()
  sleep(0.5)
  iw.oled.text("Line 2",10,10)
  iw.oled.show()
  sleep(0.5)
  iw.oled.text("Line 3",20,20)
  iw.oled.show()
  sleep(0.5)
  iw.oled.text("Line 4",30,30)
  iw.oled.show()
  sleep(0.5)
  iw.oled.text("Line 5",40,40)
  iw.oled.show()
  sleep(0.5)

  iw.oled.fill(0)
  iw.oled.set_font(umpush8pt.font)
  iw.oled.text("ภาษาไทย",0,50)
  iw.oled.show()
  sleep(0.5)
  iw.oled.fill(0)
  iw.oled.set_font(umpush10pt.font)
  iw.oled.text("ภาษาไทย",0,50)
  iw.oled.show()
  sleep(0.5)
  iw.oled.fill(0)
  iw.oled.set_font(umpush12pt.font)
  iw.oled.text("ภาษาไทย",0,50)
  iw.oled.show()
  sleep(0.5)
  iw.oled.fill(1)
  iw.oled.show()
  sleep(0.5)
  iw.oled.set_font()

  iw.oled.fill(0)
  for a in range(0,360,45):
    x1 = int(30*cos(radians(a)))+64
    y1 = int(30*sin(radians(a)))+32
    for b in range(a,360,45):
      x2 = int(30*cos(radians(b)))+64
      y2 = int(30*sin(radians(b)))+32
      iw.oled.framebuf.line(x1,y1,x2,y2,1)
  iw.oled.show()
  sleep(1)
  iw.oled.show_text("OLED test done")
  sleep(1)

def test_led():
  iw.oled.show_text("LED test start")
  sleep(1)
  for i in range(3):
    iw.oled.show_text("LED is ON")
    iw.led.value(1)
    sleep(0.5)
    iw.oled.show_text("LED is OFF")
    iw.led.value(0)
    sleep(0.5)
  iw.oled.show_text("LED test done")
  sleep(1)

def test_sw1():
  iw.oled.show_text("SW1 test start")
  sleep(1)

  iw.oled.show_text("Press and\nhold SW1")
  while iw.sw1.value() == 1:
    pass
  sleep(0.2)
  iw.oled.show_text("Release SW1")
  while iw.sw1.value() == 0:
    pass
  sleep(0.2)

  iw.oled.show_text("SW1 test done")
  sleep(1)

def test_neopixels():
  iw.oled.show_text("NeoPixels test\nstart")
  sleep(1)

  iw.oled.show_text("Showing red")
  for i in range(3):
    iw.pixel(i,(10,0,0))
  sleep(0.5)

  iw.oled.show_text("Showing green")
  for i in range(3):
    iw.pixel(i,(0,10,0))
  sleep(0.5)

  iw.oled.show_text("Showing blue")
  for i in range(3):
    iw.pixel(i,(0,0,10))
  sleep(0.5)

  iw.oled.show_text("Showing yellow")
  for i in range(3):
    iw.pixel(i,(10,10,0))
  sleep(0.5)

  iw.oled.show_text("Showing cyan")
  for i in range(3):
    iw.pixel(i,(0,10,10))
  sleep(0.5)

  iw.oled.show_text("Showing magenta")
  for i in range(3):
    iw.pixel(i,(10,0,10))
  sleep(0.5)

  iw.oled.show_text("Showing white")
  for i in range(3):
    iw.pixel(i,(10,10,10))
  sleep(0.5)

  iw.oled.show_text("Showing black")
  for i in range(3):
    iw.pixel(i,(0,0,0))
  sleep(0.5)

  iw.oled.show_text("NeoPixels test\ndone")
  sleep(1)

def test_speaker():
  iw.oled.show_text("Speaker test\nstart")
  sleep(1)
  for hz in (200,400,600,800,1000):
    iw.oled.show_text("Playing {} Hz".format(hz))
    iw.sound(hz,1)
  iw.oled.show_text("Speaker test\ndone")
  sleep(1)

def test_music():
  iw.oled.show_text("Music test\nstart")
  sleep(1)
  iw.play("""
    t180o4v100
    g8.g16a4g4>c4<b2 g8.g16a4g4>d4c2 <g8.g16>g4e4c4<b4a4 >f8.f16e4c4d4c1
  """)
  iw.oled.show_text("Music test\ndone")
  sleep(1)

def test_knob():
  while True:
    if iw.sw1.value() == 0:
      break
    iw.oled.show_text("Knob test start\nPress SW1 to end\nKnob = {}"
        .format(iw.knob.read()))
    sleep(0.1)
  iw.oled.show_text("Knob test done")
  sleep(1)

print("Start testing IPST-WiFi board...")
iw.oled.show_text("Start testing\nIPST-WiFi board")
sleep(1)
test_oled()
test_led()
test_sw1()
test_neopixels()
test_speaker()
test_music()
test_knob()
iw.oled.show_text("All tests\ncompleted")
print("IPST-WiFi board test completed.")
