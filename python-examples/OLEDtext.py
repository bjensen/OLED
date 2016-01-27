# OLEDtext.py

# This Python code is meant for use with the Raspberry Pi and Adafruit's monochrome displays!

# This program is the simplest in the whole repo. All it does is prints 3 'Hello!'s in various forms on the OLED display.
# It illustrates how to change the font size and positioning of text on the OLED... As well as showing how to do 
# basic text!

# This program was created by The Raspberry Pi Guy!

# Imports the necessary libraries... Gaugette 'talks' to the display ;-)
import gaugette.ssd1306
import time
import sys

# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display() # This clears the display but only when there is a led.display() as well!

# led.draw_text2(x-axis, y-axis, whatyouwanttoprint, size) < Understand?
# So led.drawtext2() prints simple text to the OLED display like so:

text = 'Hello!'
led.draw_text2(0,0,text,2)
text2 = 'Hello!'
led.draw_text2(0,16,text2,1)
text3 = 'Hello!'
led.draw_text2(32,25,text3,1)
led.display()
