#!/usr/bin/env bash
/usr/bin/amixer set PCM 20%

URL=http://stream.radioparadise.com/mellow-192
/usr/bin/mplayer $URL -cache 192 -nolirc -prefer-ipv4 -really-quiet -slave
