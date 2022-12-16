import time
import datetime
import os

def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        count_milliseconds = difference.microseconds / 1000
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Merry Christmas!")
            break
        else:
            os.system('cls')
            print('Until christmas there is:' + "\n" + str(difference.days) + ' days, ' + str(count_hours) +
                  ' hours, ' + str(count_minutes) + ' minutes, ' + str(count_seconds) + ' seconds, ' + str(count_milliseconds) + ' milliseconds')
            time.sleep(0.001)

if __name__ == '__main__':
    christmas = datetime.datetime(2022, 12, 25)
    countdown(christmas)