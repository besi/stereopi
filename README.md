# [stereopi][]

![image][]

Playing music on a Raspberry Pi zero

# Installation

    curl -sS https://raw.githubusercontent.com/besi/stereopi/master/bin/setup.sh | bash


# Remote control mplayer

Example

    mpc pause

Available commands

    mplayer -input cmdlist

[stereopi]: http://github.com/besi/stereopi

## Services

sudo systemctl restart raspotify.service 
sudo systemctl restart shairport-sync.service

[image]: https://raw.githubusercontent.com/besi/stereopi/master/stereopi.jpg


## Hardware

### Pinout

Encoder

	5 Down
	6 5V
	25 Up

Encoder Switch

	13 Switch
	16 GND
	

```python
import RPi.GPIO as GPIO 
from encoder import Encoder

GPIO.setmode(GPIO.BCM) 
switch_pin = 13
switch_gnd_pin = 6


encoder_up_pin = 21
encoder_common_pin = 20
encoder_down_pin = 19

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_gnd_pin, GPIO.OUT)
GPIO.setup(encoder_common_pin, GPIO.OUT)
GPIO.output(switch_gnd_pin, 0)
GPIO.output(encoder_common_pin, 1)


def valueChanged(value):
    print(value)

e1 = Encoder(encoder_up_pin, encoder_down_pin, callback=valueChanged)
````
