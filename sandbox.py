#!/usr/bin/python3 -u

import os
import time

import RPi.GPIO as GPIO

import lcd_i2c
from encoder import Encoder

GPIO.setmode(GPIO.BCM)

switch_pin = 13
encoder_down_pin = 6
encoder_up_pin = 5
minutes = 0
dirty = True
state = 'set'
mylcd = lcd_i2c.lcd()
timer_end = None


def start_timer():
    global timer_end, state
    timer_end = time.perf_counter() + (minutes * 60)
    state = 'timer'
    print("Starting timer")
    os.system('say Starting timer')


def check_timer():
    global timer_end
    remaining = int(timer_end - time.perf_counter())
    return int(remaining)

def switch_pressed(v):
    global dirty, state
    print("Pressed")

    if state == 'set':
        start_timer()
    elif state == 'done':
        state = 'set'
    dirty = True

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(switch_pin, GPIO.FALLING, callback=switch_pressed, bouncetime=500)


def update():
    global state

    if state == 'set':
        global minutes, dirty

        if not dirty: return
        mylcd.lcd_clear()
        mylcd.lcd_display_string(f"Timer:    {minutes} min", 1)

        dirty = False


    elif state == 'timer':
        mylcd.lcd_clear()
        remaining = check_timer()
        minutes = int(remaining / 60)
        seconds = remaining % 60
        mylcd.lcd_display_string(f"Timer:      {minutes}:{seconds:02d}")

    elif state == 'done':
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Timer done.")


def valueChanged(value):
    global minutes
    global dirty

    dirty = True
    minutes = max(0, value)

e1 = Encoder(encoder_down_pin, encoder_up_pin, callback=valueChanged)
update()

try:
    while True:

        if state == 'timer' and check_timer() <= 0:
            print("Timer done")
            os.system(f'say timer {minutes} minutes done')
            state = 'done'

        update()

        time.sleep(0.5)
        if state != 'set':
            time.sleep(.45)  # 0.5 + 0.45 = approx 1 second refresh rate

finally:
    print("Cleanup")
    GPIO.cleanup()
