#!/usr/bin/python3 -u

import os
import time

import RPi.GPIO as GPIO

import lcd_i2c
from encoder import Encoder

GPIO.setmode(GPIO.BCM)

os.system('say start')

switch_pin = 13
encoder_down_pin = 6
encoder_up_pin = 5
encoder_value = 0
dirty = True
pressed = True
mylcd = lcd_i2c.lcd()


def switch_pressed(v):
    global pressed, dirty
    print("OK")
    pressed = True
    dirty = True


GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(switch_pin, GPIO.FALLING)
GPIO.add_event_callback(switch_pin, switch_pressed)


def update():
    global encoder_value, dirty, pressed

    if not dirty: return
    mylcd.lcd_clear()
    mylcd.lcd_display_string(f"Encoder: {encoder_value}", 1)

    if pressed:
        mylcd.lcd_display_string("Pressed", 2)
        pressed = False
    dirty = False


def valueChanged(value):
    global encoder_value
    global dirty

    dirty = True
    encoder_value = max(0, value)
    print(encoder_value)

e1 = Encoder(encoder_down_pin, encoder_up_pin, callback=valueChanged)
update()

try:
    while True:
        update()
        time.sleep(.5)

finally:
    print("Cleanup")
    GPIO.cleanup()
