from threading import Thread
import sys
import logging
import time
import display_7segment as display

running_thread = None

def stopCountDown():
    logging.info(running_thread)
    global running_thread
    running_thread.do_run = False



def countDown(minutes):
    logging.info("in Countdown:" + str(minutes))
    global running_thread
    running_thread = Thread(target=sleeper, args=(minutes,))
    running_thread.do_run = True
    running_thread.start()


def sleeper(minutes):    
    global running_thread
    sec = minutes * 60
    timeStr = str(minutes) + ':' + str(sec % 60) 
    logging.info(str(timeStr))
    
    while ((sec > 0) and getattr(running_thread, "do_run", True)):
        time.sleep(1)
        sec = sec - 1
        mins = int(sec/60)
        secs = sec % 60
        #timeStr = str(int(sec/60)) + ':' + str(sec % 60) 
        timeStr = '{:02d}{:02d}'.format(mins, secs)
        logging.info(timeStr)
        #Write out to display
        display.writeToDisplay(timeStr)