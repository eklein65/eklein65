#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# author      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time
from numpy import array
import random

ledPin1 = 11
ledPin2 = 13
ledPin3 = 15  # define ledPins
ledPins = array([ledPin1, ledPin2, ledPin3])
buttonPin1 = 35
buttonPin2 = 37
buttonPin3 = 12
buttonPins = array([buttonPin1, buttonPin2, buttonPin3])

score = 0


def setup():
    for ledPin in ledPins:
        GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
        GPIO.setup(int(ledPin), GPIO.OUT)  # set the ledPin to OUTPUT mode
        GPIO.output(int(ledPin), GPIO.LOW)  # make ledPin output LOW level
        print('using pin%d as led' % ledPin)
    for buttonPin in buttonPins:
        GPIO.setup(int(buttonPin), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('using pin%d as button' % ledPin)


def loop():
    while True:
        for ledPin in ledPins:
            GPIO.output(int(ledPin), GPIO.HIGH)  # make ledPin output HIGH level to turn on led
            print('led turned on >>>')  # print information on terminal

        time.sleep(1)  # Wait for 1 second
        for ledPin in ledPins:
            GPIO.output(int(ledPin), GPIO.LOW)  # make ledPin output LOW level to turn off led
            print('led turned off <<<')
        time.sleep(1)  # Wait for 1 second


def whackamole():
    min = 0
    max = 2

    while True:
        randLedOn(random.uniform(min, max))


def randLedOn(sec):
    global score
    index = random.randint(0, len(ledPins - 1))
    ledPin = ledPins[index]
    buttonPin = buttonPins[index]
    GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
    print('led turned on >>>')

    timeout = sec  # [seconds]

    timeout_start = time.time()

    while time.time() < timeout_start + timeout:
        if GPIO.input(int(buttonPin)) == GPIO.LOW:  # If button pressed in time,
            GPIO.output(int(ledPin), GPIO.LOW)
            score += 1
            break

    # if user input on correct light
    #   turn off light and return with value of 1
    # else
    #   keep on full time and return with value of 0


def destroy():
    GPIO.cleanup()  # Release all GPIO


if __name__ == '__main__':  # Program entrance
    print('Program is starting ... \n')
    setup()
    try:
        whackamole()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
