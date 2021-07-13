#!/bin/sh

espeak "$*" -vde --stdout  | aplay --quiet
