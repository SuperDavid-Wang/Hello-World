# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio
import  time
import  sys

def init():  #定义初始化GPIO引脚的函数
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.IN)
    gpio.setup(35,gpio.IN)
    gpio.setup(36,gpio.IN)
    gpio.setup(37,gpio.IN)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    gpio.output(38, True)
    gpio.output(40, True)

while True:
    init()
    if gpio.input(37) == False:
        print"white"
    elif gpio.input(37) == True:
        print"black"
    time.sleep(1)
    gpio.cleanup()
