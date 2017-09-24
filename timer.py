from threading import Thread
import sys
import logging
import time


def countDown(timeToWait):
    logging.info("in Countdown:" + str(timeToWait))
    t = Thread(target=sleeper, args=(timeToWait,))
    t.start()


def sleeper(value):
    for i in range(value):
        time.sleep(1)
        logging.info(str(value -i))
        #Write out to display