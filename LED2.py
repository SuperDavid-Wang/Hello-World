# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio
import  time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7,gpio.OUT)
p = gpio.PWM(7, 100)
p.start(5)
time.sleep(5)
p.stop()
gpio.cleanup()
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7,gpio.OUT)
p = gpio.PWM(7, 100)
p.start(50)
time.sleep(5)
p.stop
gpio.cleanup()
##p=gpio.PWM(7,50)
##p.start(0)

##while True:
##    for dc in range(0, 101, 2):
##        p.ChangeDutyCycle(dc)
##        time.sleep(0.1)
##    for dc in range(100, -1, -2):
##        p.ChangeDutyCycle(dc)
##        time.sleep(0.1)
##    p.stop()
##    gpio.cleanup()
        
