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

### LCD

<https://gist.github.com/DenisFromHR/cc863375a6e19dce359d>