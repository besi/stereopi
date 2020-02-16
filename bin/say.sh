#!/bin/sh

espeak "$*" -v female3 --stdout | aplay
