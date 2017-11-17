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
    speakTimeMap = buildMapForSpeakTime(timeToEnd, speaktime)
    running_thread = timer_thread.TimerThread(timeToEnd=timeToEnd,speaktime=speakTimeMap, speakinterval=speakinterval)
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
        speakMap[secondsToTimerStr] = {"phrase" : speakItem["say"]}
        if "parms" in speakItem:
            speakMap[secondsToTimerStr]["parms"] =  speakItem["parms"]
	if "file" in speakItem:
            speakMap[secondsToTimerStr]["file"] =  speakItem["file"]

    return speakMap
def timeInSecondsOfSpeech(timeInMinutes, timeToEnd):
    minutes = timeInMinutes
    seconds = 0
    if ":" in timeInMinutes:
        splitTimeInMinutes = timeInMinutes.split(":")
        minutes = splitTimeInMinutes[0]
        seconds = splitTimeInMinutes[1]
    
    timeInSec = int(minutes) * 60
    timeInSec+=int(seconds)
    return timeToEnd - timeInSec



def buildMapForSpeakInterval(speakIntervalList):
    #take input list and create dict of time and saying
    speakIntervalMap = {}
    for speakItem in speakIntervalList:
        speakIntervalMap[speakItem["interval"]] = speakItem["say"]

    return speakIntervalMap



