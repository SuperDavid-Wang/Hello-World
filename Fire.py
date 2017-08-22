# -*- coding: utf-8 -*-
##字符串编码为utf-8格式，可以处理中文字符

import urllib,urllib2  ##读取网页数据
import json            ##在字符串数据和字典数据间进行转换
import base64          ##将非ASCII数据转换为ASCII数据
import sys             ##系统模块，用于程序和python解释器的交互
import os              ##系统模块，用于程序和操作系统的交互
import serial          ##串口通信
import string          ##字符串操作
import binascii        ##二进制数据和ASCII数据间的转换
import time            ##操作时间
import pygame
import random
import atexit
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



