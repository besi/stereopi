import datetime
import os
import time
from datetime import datetime, time
from time import sleep

is_active = False


def wait_start(runTime):
    alarm = time(*(map(int, runTime.split(':'))))
    now = datetime.today().time()
    
    while alarm.hour != now.hour and alarm.minute != now.minute:
        now = datetime.today().time()
        sleep(15)

    os.system('say good morning it is %s and %s minutes' %(now.hour, now.minute))
    os.system('sudo systemctl restart tuner')


def set_alarmclock(time):
    wait_start(time)
