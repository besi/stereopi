#!/usr/bin/python3 -u

import time
import board
import neopixel
import math
import RPi.GPIO as GPIO

pixels = neopixel.NeoPixel(board.D18,1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)


# Read input pin 12 which is the switch

print("Starting...")
x = 0
increment = 0.1
sleep = 0.01
dimmer = .04

while True:

  if GPIO.input(12) == 0:
     dimmer = 1 - dimmer
     time.sleep(.2)
  blue = abs(int(math.sin(x)*255*dimmer))
  red = abs(int(math.cos(x)*255*dimmer))
  # green = abs(int(math.cos(x + math.pi/4)*255*dimmer))
  pixels[0] = (red,0,blue)
  x = x + increment
  time.sleep(sleep)

