from ipstw_ku import ipstw as iw
from time import sleep

iw.oled.set_font()
iw.oled.show_text(">>> READY <<<")
sleep(2)

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
iw.oled.text("Line 6",50,50)
iw.oled.show()
sleep(0.5)
