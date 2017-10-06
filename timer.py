import logging
import timer_thread

running_thread = None

def stopCountDown():
    if running_thread is not None:
        logging.info(running_thread)
        global running_thread
        running_thread.do_run = False



def countDown(timeToEnd):
    logging.info("in Countdown:" + str(timeToEnd))
    global running_thread
    if running_thread is not None:
        running_thread.stop()
    running_thread = timer_thread.TimerThread(timeToEnd=timeToEnd)
    running_thread.start()

