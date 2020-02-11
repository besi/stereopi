#!/usr/bin/python3 -u

import math
import time

import RPi.GPIO as GPIO
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Read input pin 12 which is the switch

print("Starting...")
x = 0
increment = 0.1
sleep = 0.01
dimmer = .04

from remote_service import RemoteService


def on_key_pressed(key):
    print(key)
    if key == 'KEY_RED':
        pixels[0] = (int(255 * dimmer), 0, 0)
    elif key == 'KEY_GREEN':
        pixels[0] = (0, int(255 * dimmer), 0)
    elif key == 'KEY_YELLOW':
        pixels[0] = (int(255 * dimmer), int(255 * dimmer), 0)
    elif key == 'KEY_BLUE':
        pixels[0] = (0, 0, int(255 * dimmer))
    elif key == 'KEY_PLAYPAUSE':
        pixels[0] = (0, 0, 0)
    else:
        pixels[0] = (int(255 * dimmer), 0, int(255 * dimmer))
    elif key == 'KEY_VOLUMEUP':
        os.system("amixer set PCM 5%+")
    elif key == 'KEY_VOLUMEDOWN':
        os.system("amixer set PCM 5%-")


service = RemoteService()
service.start_listening(on_key_pressed)

while True:

    if GPIO.input(12) == 0:
        dimmer = 1 - dimmer
        time.sleep(.2)
    blue = abs(int(math.sin(x) * 255 * dimmer))
    red = abs(int(math.cos(x) * 255 * dimmer))
    # green = abs(int(math.cos(x + math.pi/4)*255*dimmer))
    pixels[0] = (red, 0, blue)
    x = x + increment
    time.sleep(sleep)
