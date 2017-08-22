# -*- coding: utf-8 -*-
##字符串编码为utf-8格式，可以处理中文字符

import time            ##操作时间
import RPi.GPIO as gpio

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    gpio.setup(11,gpio.IN)
    gpio.setup(7,gpio.OUT)
    
while True:
    init()
    if gpio.input(11)==True:
        gpio.output(7,False)
        gpio.cleanup()
    else:        
        os.system("mpg123 fire.mp3")
        gpio.output(7,True)
        time.sleep(3)
        gpio.cleanup()



