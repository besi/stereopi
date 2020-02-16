import datetime
import os
import time

is_active = False

from datetime import datetime, time
from time import sleep

def wait_start(runTime):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time():  # you can add here any additional variable to break loop if necessary
        sleep(15)

    os.system('say good morning')
    os.system('sudo systemctl restart tuner')


def set_alarmclock(time):
    wait_start(time)
