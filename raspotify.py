#!/usr/bin/python3

import os
import logging
logging.basicConfig(filename='/var/log/raspotify.log',level=logging.DEBUG)

event = os.environ['PLAYER_EVENT']
logging.info(f"PLAYER_EVENT = '{event}'")


if event == "start":
    logging.info("STARTED")
    os.system('sudo systemctl stop tuner')
    os.system('killall mplayer')

if event == "change":
    logging.info(os.environ['OLD_TRACK_ID'])
    logging.info(os.environ['TRACK_ID'])

if event == "stop": pass
