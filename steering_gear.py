# -*- coding: utf-8 -*-
import RPi.GPIO as gpio  
import time  
import atexit

def steer(j):
    for i in range(0,j):
        atexit.register(gpio.cleanup)
        gpio.setwarnings(False)   
        gpio.setmode(gpio.BOARD)  
        gpio.setup(31, gpio.OUT)
        gpio.output(31, False)
        p = gpio.PWM(31, 50) #50HZ  
        p.start(2.5) ##p.start(2.5) # initial position
        p.ChangeDutyCycle(6.5) #turn left for 80 degrees
        time.sleep(0.2)
        atexit.register(gpio.cleanup)
        p.ChangeDutyCycle(2.5) #turn back
        time.sleep(0.2)
        atexit.register(gpio.cleanup)
        gpio.cleanup()

steer(2)







