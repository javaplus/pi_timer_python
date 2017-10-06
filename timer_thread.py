from threading import Thread
import time
import display_7segment as display


class TimerThread(Thread):
    def __init__(self, timeToEnd):
        self.running = False
        self.timeToEnd = timeToEnd
        super(TimerThread, self).__init__()

    def start(self):
        self.running = True
        super(TimerThread, self).start()

    def run(self):
        #based on current time find how long timer should run
        currentTime = time.time()
         #get what the endtime should be
        secsToEnd = self.timeToEnd - currentTime
        
        sec = secsToEnd # initialize total current secs to total
        minutes = int(sec/60)
        #build initial timer string:
        timeStr = str(minutes) + ':' + str(sec % 60) 
        #logging.info("Initial time String:" + str(timeStr))
       
        #global is7SegmentDisplayAvailable

        while ((sec > 1) and (self.running is True)):
            
            sec = secsToEnd - time.time() # seconds left should be endTime - current time
            mins = int(sec/60)
            secondsForTimer = int(sec % 60)
            #timeStr = str(int(sec/60)) + ':' + str(sec % 60) 
            timeStr = '{:02d}{:02d}'.format(mins, secondsForTimer)
            
            #Write out to display
            display.writeToDisplay(timeStr)
            time.sleep(.25) # wait 1/4 a second before checking time again

    def stop(self):
        self.running = False