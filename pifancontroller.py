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
# - Introduced 'minTemp' and 'maxTemp' logic
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
maxTemp = 60
# The min CPU temperature in Celsius before the fan is turned off
# Must be a smaller value than 'maxTemp'
minTemp = 50


# TEMPERATURE READ FUNCTION #
def currentTemp():
    # Save the command output of 'vcgencmd measure_temp'
    commandOutput = popen("vcgencmd measure_temp").readline()
    # Cleanup output and convert it to a float point number
    CPUtemp = float(commandOutput.replace("temp=", "").replace("'C\n", ""))
    # Uncomment the line below for testing
    # print("Current temperature is {0}".format(CPUtemp))
    return CPUtemp


# MAIN SCRIPT #
try:
    fan = OutputDevice(pin)
    while True:
        if currentTemp() > maxTemp:
            fan.on()
        elif currentTemp() < minTemp:
            fan.off()
        sleep(frequency)
except KeyboardInterrupt:
    print("\npifancontroller.py quit")
