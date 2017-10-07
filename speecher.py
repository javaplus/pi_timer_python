


def getPhraseToSay(listOfTimes,currentTime):
    for key in listOfTimes:
        if key == str(currentTime):
            return listOfTimes[key]

def speak(listOfTimes, currentTime):
    phrase = getPhraseToSay(listOfTimes, currentTime)
    if phrase:
        print("Speaking:" + phrase)
