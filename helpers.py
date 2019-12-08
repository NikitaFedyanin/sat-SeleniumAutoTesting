import time
import datetime

def delay(duration, description=None):
    time.sleep(duration)

def log(description):
    current_time = datetime.datetime.now()

    print('{time}        {desc}'.format(time=current_time, desc=description))