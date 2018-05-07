# pi_timer_python

Code for the Distrubuted timer boxes that make up the "Game Commander" system.

This code is used to control Adafruit's 7 segment display with I2C backpack as well as control speaking commands.

## display_7segment.py

This module is the module that imports the Adafruit_LED_Backpack module to write out to the 7 segment display.

It simply writes a value out to the display and optionaly writes out the colon


## mqtt_server.py

The main entry point into the timer boxes.  This is the code that connects to a topic/queue and listens for a message.

When a message is dropped on the timer queue it processes the message and starts the timer countdown

Uses the environment variable "pi_server_ip" to set the server ip.

## server.py

Due to the fact I'm  adding documentation months after development, combined with the fact I left a few junk programs around... I'm not entirely sure the purpose of this module. I believe this was a simple REST API to test the individual boxes timer funtions directly without have a server present or using MQTT. Early on in development this was used to test the timer functionality by sending a number of minutes to the timer module just to test the display logic.  I'm pretty certain it's not used at all during runtime.

## speech_server.py

Used to listen to the speech/talk topic for messages that it should speak/play immediately regardless of the state of the timer.

Uses the environment variable "pi_server_ip" to set the server ip where the topic is located.



## timer.py

The core logic for the speaking and timer functionality.  It takes the time to end and the list of speak times and parses them to calculate the precise times that the timer should be and when phrases should be spoken.  It then spawns a thread to process the current timer message.  This way it can continue to listen in case another timer message comes in.  In the case, that another timer request comes in while one is started, this module will kill the currently running thread before starting the new timer thread.

NOTE: The speak interval functionality is not fully implemented yet.


## timer_thread.py

The module that runs to calculate what should be written out the display based on the current system time and the endtime of the timer.  Also, issues the speaking commands based on the speaking map that is passed to it.

NOTE: speakinterval is not used at this time.  It is a place holder for a possible future enhancement that allows a parameterized message to be spoken at specific intervals. The idea is that this allows you to specify one entry for a message that is repeated multiple times during the countdown of the timer.  For Example: If you wanted the timer to speak "15 mintues remaining", "10 minutes remaining", and "5 minutes remaining", instead of having 3 entries in the speaktime collection, you would pass one entry to to speakinterval that was something like: "%min% minutes remaining".  That's the idea anyway.   



