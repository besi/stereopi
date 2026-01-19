#!/usr/bin/env bash
/usr/bin/amixer set PCM 20%

URL=https://stream.radioparadise.com/rock-flac

URL=http://stream.radioparadise.com/mellow-128

URL=http://stream.radioparadise.com
URL=http://stream-uk1.radioparadise.com/aac-128
URL=http://stream-uk1.radioparadise.com/aac-320
URL=https://stream.radioparadise.com/flac

/usr/bin/mplayer $URL -cache 192 -nolirc -prefer-ipv4 -really-quiet -slave
