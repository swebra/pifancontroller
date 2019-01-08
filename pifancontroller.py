#!/usr/bin/env python3

# Author: imswebra
# 06-2018
# http://www.imswebra.com/pifancontroller
#
# Based off script by Edoardo Paolo Scalafiotti, found below:
# https://web.archive.org/web/20180604025525/https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c
#
# Changes
# - Rewrote using 'gpiozero' library
# - Removed unnecessary dependencies
# - Renamed function and variable names
# - Introduced 'mintemp' and 'maxtemp' logic
# - Added 'frequency' variable
# - Improved comments


# IMPORTS #
from gpiozero import OutputDevice
from os import popen
from time import sleep


# USER VARIABLES #

# The GPIO pin ID connected to the transistor's base. (BCM #)
pin = 14
# The frequency in seconds at which the temperature is checked
frequency = 10

# Defining two points allows for the temperature to oscillate within a
# controlled threshold instead of rapidly turning on and off as the
# temperature tries to stabilize around a single point. The larger the
# difference between the two values, the longer the periods of on and
# off will be while operating in this region.

# The max CPU temperature in Celsius before the fan is turned on
maxtemp = 60
# The min CPU temperature in Celsius before the fan is turned off
# Must be a smaller value than 'maxtemp'
mintemp = 50


# TEMPERATURE READ FUNCTION #
def currenttemp():
    # Save the command output of 'vcgencmd measure_temp'
    commandoutput = popen("vcgencmd measure_temp").readline()
    # Cleanup output and convert it to a float point number
    CPUtemp = float(commandoutput.replace("temp=", "").replace("'C\n", ""))
    # Uncomment the line below for testing
    # print("Current temperature is {0}".format(CPUtemp))
    return CPUtemp


# MAIN SCRIPT #
try:
    fan = OutputDevice(pin)
    while True:
        if currenttemp() > maxtemp:
            fan.on()
        elif currenttemp() < mintemp:
            fan.off()
        sleep(frequency)
except KeyboardInterrupt:
    print("\nfancontrol.py quit")
