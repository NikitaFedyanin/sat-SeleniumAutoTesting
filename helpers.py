import time
import datetime


def delay(duration, description=None):
    time.sleep(duration)
    description = description if description else 'Ожидание - {} секунд'.format(duration)
    log(description)


def log(description):
    current_time = datetime.datetime.now()

    print('{time}        {desc}\n'.format(time=current_time, desc=description))


