from threading import Thread
import time
import display_7segment as display


class TimerThread(Thread):
    def __init__(self, minutes):
        self.running = False
        self.minutes = minutes
        super(TimerThread, self).__init__()

    def start(self):
        self.running = True
        super(TimerThread, self).start()

    def run(self):
        sec = self.minutes * 60
        #build initial timer string:
        timeStr = str(self.minutes) + ':' + str(sec % 60) 
        #logging.info("Initial time String:" + str(timeStr))
        #get current system time
        startTimeInSeconds = time.time()
        #get what the endtime should be
        endTimeInSeconds = startTimeInSeconds + sec
        global is7SegmentDisplayAvailable

        while ((sec > 1) and (self.running is True)):
            
            sec = endTimeInSeconds - time.time() # seconds left should be endTime - current time
            mins = int(sec/60)
            secondsForTimer = int(sec % 60)
            #timeStr = str(int(sec/60)) + ':' + str(sec % 60) 
            timeStr = '{:02d}{:02d}'.format(mins, secondsForTimer)
            
            #Write out to display
            display.writeToDisplay(timeStr)
            time.sleep(.25) # wait 1/4 a second before checking time again

    def stop(self):
        self.running = False