from threading import Thread
import time
import speecher
import global_event_emmitter

try:
    import display_7segment as display
except BaseException as ex:
    print(ex.message)
    pass


class TimerThread(Thread):
    def __init__(self, timeToEnd, speaktime, speakinterval):
        self.running = False
        self.timeToEnd = timeToEnd
        self.speaktime = speaktime
        self.speakinterval = speakinterval
        super(TimerThread, self).__init__()

    def start(self):
        self.running = True
        super(TimerThread, self).start()

    def run(self):
        # based on current time find how long timer should run
        currentTime = time.time()
        # get what the endtime should be
        secsToEnd = self.timeToEnd - currentTime
        #print("secsToEnd=" + str(secsToEnd))

        sec = secsToEnd  # initialize total current secs to total
        #print("Sec=" + str(sec))
        minutes = int(sec/60)
        # build initial timer string:
        timeStr = str(minutes) + ':' + str(sec % 60)
        #print("Time Str" + timeStr)
        #logging.info("Initial time String:" + str(timeStr))

        while ((sec > -5) and (self.running is True)):

            currentTime = int(time.time())
            # seconds left should be endTime - current time
            sec = self.timeToEnd - currentTime
            #print("Secs=" + str(sec))
            mins = int(sec/60)
            secondsForTimer = int(sec % 60)
            #timeStr = str(int(sec/60)) + ':' + str(sec % 60)
            if sec < 1:
                timeStr = '0000'
            else:
                timeStr = '{:02d}{:02d}'.format(mins, secondsForTimer)
                #print("timeStr=" + timeStr)

            try:
                # see if we can speak:
                speecher.speak(self.speaktime, currentTime)
                # Don't stop keeping time if we can't speak
                # so catch the exception
            except BaseException as ex:
                print("Error speaking: " + ex.message)
            # TODO: speak for intervals

            try:
                # Write out to display
                display.writeToDisplay(timeStr)
            except BaseException as ex:
                # If can't write to display keep going
                print("Error writing to display: " + ex.message)
                pass

            time.sleep(.25)  # wait 1/4 a second before checking time again
        
        global_event_emmitter.broadcastEvent("timer_stopped")
        

    def stop(self):
        self.running = False
