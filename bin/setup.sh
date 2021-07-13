#!/usr/bin/env bash

sudo apt update
sudo apt upgrade

# Install I2S driver
# WARNING: Only install the anti-pop-service if there is no Mems  mic attached
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash

# REBOOT


#### Sourcecode + say command
sudo apt install git
git clone https://github.com/besi/stereopi.git && cd stereopi
sudo ln -s $HOME/stereopi/bin/say.sh /usr/bin/say
chmod +x /usr/bin/say
/usr/bin/say installed espeak

sudo apt install screen python3-pip espeak -y
say Done installing the essentials

#### PIP
screen -S pip
#  NeoPixel support requires running with sudo
sudo pip3 install paho-mqtt evdev install rpi_ws281x adafruit-circuitpython-neopixel
/usr/bin/say installed python packages
# CTRL + A + D to exit out of the screen

#### APT
screen -S apt
sudo apt install mplayer python3 python3-dbus mosquitto mosquitto-clients -y
/usr/bin/say installed a.p.t. packages
# CTRL + A + D to exit out of the screen

#### Raspotify
screen -S raspotify
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
touch /var/log/raspotify.log
sudo ln -s /var/log/raspotify.log /home/pi/stereopi/log/raspotify.log
sudo chown pi:pi /home/pi/stereopi/log/raspotify.log
# CTRL + A + D to exit out of the screen


#### Shairport AIRport support
screen -S airplay
# Install shairport-sync for Airplay playback
sudo apt-get install autoconf automake avahi-daemon build-essential libasound2-dev libavahi-client-dev libconfig-dev libdaemon-dev libpopt-dev libssl-dev libtool xmltoman -y
cd
git clone https://github.com/mikebrady/shairport-sync.git
cd shairport-sync
autoreconf -i -f
./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata --with-libdaemon --with-mqtt-client
make
sudo make install
sudo systemctl start shairport-sync
say airplay done
# CTRL + A + D to exit out of the screen


#### Stereopi SETUP
screen -S stereopi
# Startup the stereopi at boot
cd ~/stereopi
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
say stereopi done
# CTRL + A + D to exit out of the screen


# Setup display
cd ~/stereopi
sudo cp dist/etc/systemd/system/stereopi-display.service /etc/systemd/system/
sudo systemctl daemon-reload
python3 -m pip install smbus
sudo systemctl start stereopi-display

### Bluetooth
screen -S bluetooth
VERSION=bluez-5.59
date 
sudo apt-get install libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev python-docutils-y
date
wget www.kernel.org/pub/linux/bluetooth/$VERSION.tar.xz &&  tar xvf $VERSION.tar.xz && 

date
cd $VERSION 
./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc --localstatedir=/var --enable-experimental
make -j4
sudo make install
date
say bluetooth installed please reboot
sudo reboot

# Set the timezone and the locale
screen -S locale
sudo raspi-config

