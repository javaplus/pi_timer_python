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

Due to the fact I'm  adding documentation months after development, combined with the fact I left a few junk programs around... I'm not entirely sure the purpose of this module. I believe this was a simple REST API to test the individual boxes timer funtions directly without have a server present or using MQTT. Early on in development this was used to test the timer functionality by sending a number of minutes to the timer module.  I'm pretty certain it's not used at all during runtime.

## speech_server.py

Used to listen to the speech/talk topic for messages that it should speak/play immediately regardless of the state of the timer.

Uses the environment variable "pi_server_ip" to set the server ip where the topic is located.



## timer.py

The core logic for the speaking and timer functionality.  It takes the time to end and the list of speak times and parses them to calculate the precise times that the timer should be and when phrases should be spoken.

NOTE: The speak interval functionality is not fully implemented yet.


