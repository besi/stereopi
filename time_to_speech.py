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
    start = 'It is'
    accuracies = ['exactly', '']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    min = ['ten', 'twenty', 'thirty', 'fourty', 'fifty']
    suffixes = ['in the morning', 'in the afternoon', 'in the evening', 'at night']

    ## - define random strings

    hour = numbers[(int(hours) - 1) % 12]

    if round(int(minutes), -1) == 0 or round(int(minutes), -1) == 60:
        random_middle = ''
    else:
        random_middle = min[int((round(int(minutes), -1) / 10)) - 1]

    ## -define for final ex)its , it's , almost, one two three..

    if 4 <= hours < 12:
        ending = 'in the morning'
    elif 12 <= hours < 18:
        ending = 'in the afternoon'
    elif 18 <= hours < 21:
        ending = 'in the evening'
    elif 21 <= hours <= 23 or 0 <= hours < 4:
        ending = 'at night'

    if hours == 0 and minutes == 0:
        result = "It's midnight"
    elif hours == 12 and minutes == 0:
        print('nooon')
        result = "It's %s noon" % random.choice(accuracies)
    elif minutes == 0:
        result = "%s %s 'o clock %s" % (start, hour, ending)
    elif minutes % 10 == 0:
        result = "%s %s %s past %s %s" % (start, random.choice(accuracies), random_middle, hour, ending)
    elif round(int(minutes), -1) == 0:
        result = "%s roughly %s %s %s" % (start, random_middle, hour, ending)
    elif round(int(minutes), -1) == 60:
        next_hour = numbers[hours % 12]
        result = "%s roughly %s %s %s" % (start, random_middle, next_hour, ending)
    else:
        result = "%s roughly %s minutes after %s %s" % (start, random_middle, hour, ending)
    return result


print(ishtime(hour, minute))
