#!/bin/sh

espeak "$1" -vde --stdout | aplay -D 'plughw:1'
