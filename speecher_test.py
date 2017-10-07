import unittest
import time
import speecher

class TimerTest(unittest.TestCase):

    def testCanFindPhraseToSay(self):
        listOfTimes = {}
        currentTime = time.time()
        # set the time to speak as 1 minute from now
        timeToSpeak = currentTime + 60
        #print("timetoSpeak="+ str(timeToSpeak))
        listOfTimes[str(timeToSpeak)] = "GO"
        # call method under test and tell it is the time to speak

        phrase = speecher.getPhraseToSay(listOfTimes, timeToSpeak)

        self.assertEqual("GO", phrase)

    def testCanary(self):
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()