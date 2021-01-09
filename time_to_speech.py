# Credits go to <http://codereview.stackexchange.com/q/37522>
import random
import time


def current_time():
    '''Returns a tuple containing (hour, minute) for current local time.'''
    local_time = time.localtime(time.time())
    return (local_time.tm_hour, local_time.tm_min)


(hour, minute) = current_time()


def ishtime(hours, minutes):
    hours = hours % 24
    return(str(hours) + ' and ' + str(minutes) + 'minutes')


print(ishtime(hour, minute))
