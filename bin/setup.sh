#!/usr/bin/env bash

# Install I2S driver
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash

# curl -sS https://raw.githubusercontent.com/besi/stereopi/master/bin/setup.sh | bash
sudo apt install git -y
git clone https://github.com/besi/stereopi.git && cd stereopi

# Install say binary
sudo apt install espeak -y
sudo ln -s $HOME/stereopi/bin/say.sh /usr/bin/say
chmod +x /usr/bin/say
/usr/bin/say installed espeak

# This needs to be run from the root of the project
sudo apt install mplayer -y
sudo apt install screen -y
sudo apt install python3 python3-pip python3-dbus -y

#  NeoPixel support requires running with sudo
sudo pip3 install paho-mqtt
sudo pip3 install evdev
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
/usr/bin/say installed python packages

# Disable the popping of the speaker (We don't have an I2S mic so it's fine)
sudo cp dist/etc/systemd/system/aplay.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable aplay

# Startup the stereopi at boot
sudo cp dist/etc/systemd/system/stereopi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable stereopi

# Startup the radio at boot
sudo cp dist/etc/systemd/system/tuner.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tuner

# mplayer remote control file
mkdir -p $HOME/.mplayer
mkfifo $HOME/.mplayer/fifo
cp dist/homedir/.mplayer/config $HOME/.mplayer/
sudo ln -s $HOME/stereopi/bin/mpc.sh /usr/bin/mpc
sudo chmod +x /usr/bin/mpc
