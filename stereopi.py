#!/usr/bin/python3 -u
import math
import os
import threading
import time

import RPi.GPIO as GPIO
import board
import neopixel

import wakeup

switch_pin = 13
led_pin = board.D12

pixels = neopixel.NeoPixel(led_pin, 1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Starting...")
dimmer = .04

from remote_service import RemoteService


def run_alarm(time):
    wakeup.set_alarmclock(time)


def set_alarm(alarm):
    threading.Thread(target=run_alarm, args=(alarm,)).start()


def timer():
    timer_mins = 20
    os.system('sudo systemctl start tuner')
    os.system(f"say Timer {timer_mins} minutes")
    time.sleep(timer_mins * 60)
    os.system('sudo systemctl stop tuner')


def start_timer():
    threading.Thread(target=timer).start()


def on_key_pressed(key):
    print(key)
    if key == 'KEY_': pass
    if key == 'KEY_FASTFORWARD': os.system('curl -X POST "https://api.spotify.com/v1/me/player/next" -H "Authorization: Bearer BQDy-sPybW8wtFbDhA9VfbTN1PSnoNZ6RHTzQrykoQgbvSXiSjbpotv3Tx6QzVzFt0WtNYXBgANRULfVczCpq9tjNfw_wpSMRwFNhW4fLyBXODHcs-r_C8JSQwyhcSIHdjS7ntgGE7scyAg" &')
    if key == 'KEY_REWIND': os.system('curl -X POST "https://api.spotify.com/v1/me/player/previous" -H "Authorization: Bearer BQDy-sPybW8wtFbDhA9VfbTN1PSnoNZ6RHTzQrykoQgbvSXiSjbpotv3Tx6QzVzFt0WtNYXBgANRULfVczCpq9tjNfw_wpSMRwFNhW4fLyBXODHcs-r_C8JSQwyhcSIHdjS7ntgGE7scyAg" &')

    if key == 'KEY_SEARCH':
         os.system('say `sudo python3 /home/pi/stereopi/time_to_speech.py` &')
    elif key == 'KEY_RED':
        pixels[0] = (int(255 * dimmer), 0, 0)
    elif key == 'KEY_GREEN':
        pixels[0] = (0, int(255 * dimmer), 0)
    elif key == 'KEY_YELLOW':
        pixels[0] = (int(255 * dimmer), int(255 * dimmer), 0)
    elif key == 'KEY_BLUE':
        pixels[0] = (0, 0, int(255 * dimmer))
    elif key == 'KEY_PLAYPAUSE':
        pixels[0] = (0, 0, 0)
        os.system('/usr/bin/mpc pause &')
    elif key == 'KEY_VOLUMEUP':
        os.system("amixer set PCM 5%+")
    elif key == 'KEY_INFO':
        os.system("sudo systemctl stop tuner")
        os.system("sudo systemctl restart shairport-sync")
        os.system("sudo systemctl restart raspotify")
    elif key == 'KEY_TUNER':
        os.system('sudo systemctl restart raspotify')
        os.system("sudo systemctl restart tuner")
        os.system("say starting tuner")
    elif key == 'KEY_VOLUMEDOWN':
        os.system("amixer set PCM 5%-")
    elif key == 'KEY_NEXTSONG':
        start_timer()
    elif key == 'KEY_HOMEPAGE':
        alarm = '6:15'
        os.system(f"say setting alarm to {alarm}")
        set_alarm(alarm)
    else:
        pixels[0] = (int(255 * dimmer), 0, int(255 * dimmer))


service = RemoteService()
service.start_listening(on_key_pressed) # This call is blocking so we never come here

x = 0
increment = 0.1
sleep = 0.01

while True:

    if GPIO.input(switch_pin) == 0:
        pixels[0] = (0, 0, int(255 * dimmer))
    blue = abs(int(math.sin(x) * 255 * dimmer))
    red = abs(int(math.cos(x) * 255 * dimmer))
    # green = abs(int(math.cos(x + math.pi/4)*255*dimmer))
    pixels[0] = (red, 0, blue)
    x = x + increment
    time.sleep(sleep)
