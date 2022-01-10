#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time
from numpy import array

ledPin1 = 11
ledPin2 = 13
ledPin3 = 15 # define ledPins
ledPins = [ledPin1, ledPin2, ledPin3]

def setup(ledPin):
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('using pin%d'%ledPin)

def loop():
    while True:
        for ledPin in ledPins:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(.2)
            GPIO.output(ledPin, GPIO.LOW)# make ledPin output HIGH level to turn on led
        
def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup(ledPin1)
    setup(ledPin2)
    setup(ledPin3)
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        for ledPin in ledPins:
            GPIO.output(ledPin, GPIO.LOW)
        destroy()

