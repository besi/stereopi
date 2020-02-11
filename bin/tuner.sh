#!/usr/bin/env bash
/usr/bin/amixer set PCM 30%
/usr/bin/mplayer -prefer-ipv4 -cache 128 -playlist http://www.radioparadise.com/musiclinks/rp_128aac.m3u -noconsolecontrols -really-quiet -nolirc
