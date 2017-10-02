import logging
import time
import display_7segment as display
import timer_thread

running_thread = None

def stopCountDown():
    if running_thread is not None:
        logging.info(running_thread)
        global running_thread
        running_thread.do_run = False



def countDown(minutes):
    logging.info("in Countdown:" + str(minutes))
    global running_thread
    if running_thread is not None:
        running_thread.stop()
    running_thread = timer_thread.TimerThread(minutes=minutes)
    running_thread.start()



def timeKeeper(minutes):    
    global running_thread
    sec = minutes * 60
    #build initial timer string:
    timeStr = str(minutes) + ':' + str(sec % 60) 
    #logging.info("Initial time String:" + str(timeStr))
    #get current system time
    startTimeInSeconds = time.time()
    #get what the endtime should be
    endTimeInSeconds = startTimeInSeconds + sec
    global is7SegmentDisplayAvailable

    while ((sec > 1) and getattr(running_thread, "do_run", True)):
        
        sec = endTimeInSeconds - time.time() # seconds left should be endTime - current time
        mins = int(sec/60)
        secondsForTimer = int(sec % 60)
        #timeStr = str(int(sec/60)) + ':' + str(sec % 60) 
        timeStr = '{:02d}{:02d}'.format(mins, secondsForTimer)
        
        #Write out to display
        display.writeToDisplay(timeStr)
        time.sleep(.25) # wait 1/4 a second before checking time again
