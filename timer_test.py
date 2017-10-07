import unittest
import json
import timer
import time

class TimerTest(unittest.TestCase):

    def testTimeInSecondsOfSpeech(self):
        
        timeToEnd = time.time() + 600 # 10 minute timer
        timeInMinutesToAlarm = "1"
        timeOfAlarm = timer.timeInSecondsOfSpeech(timeInMinutesToAlarm,timeToEnd)

        expectedTimeOfAlarm = timeToEnd - 60
        self.assertEqual(expectedTimeOfAlarm, timeOfAlarm)

    def testBuildMapForSpeakTimeTest(self):
        
        #set the time to end to be 5 minutes from now
        currentTime = time.time()
        timeToEnd =  currentTime + (5 *60) 

        inputData = '{"speaktime":[{"time":"5", "say":"GO"}, {"time":"1","say":"1 minute remaining"}]}'
        #inputData = '{"speaktime":"123"}'
        inputData = json.loads(inputData)

        speakTimeList = inputData["speaktime"]

        #print("inputData:" + speakTimeList[0]["time"] )
        
        
        speakTestMap = timer.buildMapForSpeakTime(timeToEnd, speakTimeList) 

        strTime = str(currentTime)

        # since our test data is a five minute timer, then it should have an entry for current time
        self.assertEqual(speakTestMap[strTime], "GO")
        #self.assertEqual(speakTestMap["1"], "1 minute remaining")


    def testBuildMapForSpeakIntervalTest(self):
        
        inputData = '{"speakinterval":[{"interval":"5", "say":"%min% Minutes Remaining, %min% Minutes."}]}'
        inputData = json.loads(inputData)

        speakTimeList = inputData["speakinterval"]

        
        speakIntervalMap = timer.buildMapForSpeakInterval(speakTimeList) 

        
        self.assertEqual(speakIntervalMap["5"], "%min% Minutes Remaining, %min% Minutes.")
       


if __name__ == '__main__':
    unittest.main()