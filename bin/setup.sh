#!/usr/bin/env bash

# This needs to be run from the root of the project

pip3 install paho-mqtt
pip3 install evdev
pip3 install rpi_ws281x adafruit-circuitpython-neopixel


# Disable the popping of the speaker (We don't have an I2S mic so it's fine)
sudo cp dist/etc/systemd/system/aplay.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable aplay

# Startup the stereopi at boot
sudo cp dist/etc/systemd/system/stereopi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable stereopi