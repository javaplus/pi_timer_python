import os
import threading


def getPhraseToSay(listOfTimes,currentTime):
    for key in listOfTimes:
	#print("key=" + key)
        #print("curTime=" + str(currentTime))
        if key == str(currentTime):
            return listOfTimes.pop(key,None)

def speak(listOfTimes, currentTime):
    phrase = getPhraseToSay(listOfTimes, currentTime)
    if phrase:
        print("Speaking:" + phrase["phrase"])
        t = threading.Thread(target=worker, args=(phrase,))
        t.start()
	
        
def worker(phrase):

    os.system("espeak " + phrase["parms"] + " \"" + phrase["phrase"] + "\"") 
    
