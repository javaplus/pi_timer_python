


def getPhraseToSay(listOfTimes,currentTime):
    for key in listOfTimes:
        if key == str(currentTime):
            return listOfTimes[key]

