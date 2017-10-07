import logging
import timer_thread

running_thread = None

def stopCountDown():
    if running_thread is not None:
        logging.info(running_thread)
        global running_thread
        running_thread.do_run = False



def countDown(timeToEnd,speaktime,speakinterval):
    logging.info("in Countdown:" + str(timeToEnd))
    global running_thread
    if running_thread is not None:
        running_thread.stop()
    running_thread = timer_thread.TimerThread(timeToEnd=timeToEnd)
    running_thread.start()

def buildMapForSpeakTime(timeToEnd, speaktimeList):
    #take input list and create dict of time and saying
    # calculate time
    speakMap = {}
    for speakItem in speaktimeList:
        timeOfItem = speakItem["time"] # this might say at the 10 minute mark
        
        #find future time for time in list
        secondsToTimer = timeInSecondsOfSpeech(timeOfItem, timeToEnd)
        secondsToTimerStr = str(secondsToTimer)
        print("timeToSpeak=" + secondsToTimerStr)
        speakMap[secondsToTimerStr] = speakItem["say"]

    return speakMap
def timeInSecondsOfSpeech(timeInMinutes, timeToEnd):
    timeInSec = int(timeInMinutes) * 60
    return timeToEnd - timeInSec



def buildMapForSpeakInterval(speakIntervalList):
    #take input list and create dict of time and saying
    speakIntervalMap = {}
    for speakItem in speakIntervalList:
        speakIntervalMap[speakItem["interval"]] = speakItem["say"]

    return speakIntervalMap



