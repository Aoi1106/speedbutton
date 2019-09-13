#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setmode(2,GPIO.OUT)
GPIO.setmode(3,GPIO.OUT)
GPIO.setmode(4,GPIO.OUT)
GPIO.setmode(17,GPIO.OUT)

GPIO.setmode(7,GPIO.IN)
GPIO.setmode(8,GPIO.IN)
GPIO.setmode(25,GPIO.IN)
GPIO.setmode(24,GPIO.IN)
GPIO.setmode(23,GPIO.IN)

while True:

    GPIO.output(2,False)
    GPIO.output(3,False)
    GPIO.output(4,False)
    GPIO.output(17,False)

    while True:
        if GPIO.input(7):
            GPIO.output(2,True)
            break
        if GPIO.input(8):
            GPIO.output(3,True)
            break
        if GPIO.input(25):
            GPIO.output(4,True)
            break
        if GPIO.input(24):
            GPIO.output(17,True)
            break

    while True:
        if GPIO.input(23):
            break

GPIO.cleanup