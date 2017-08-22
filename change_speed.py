# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio
import  time
import  sys
import pygame
import atexit
from zhinanzhen import *

gpio.setwarnings(False)

def forward(speed,t):
    atexit.register(gpio.cleanup)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.output (12, True)  #让右电机逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    left=gpio.PWM(38,20)
    right=gpio.PWM(40,20)
    left.start(speed)
    right.start(speed)
    time.sleep(t)
    gpio.cleanup()

def backward(speed,t):
    atexit.register(gpio.cleanup)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  
    gpio.output(7,True)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    left=gpio.PWM(38,20)
    right=gpio.PWM(40,20)
    left.start(speed)
    right.start(speed)
    time.sleep(t)
    gpio.cleanup()

def pivot_turn_right(speed,t):
    atexit.register(gpio.cleanup)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机不顺转
    gpio.output (22, True)  #让左电机 顺转
    gpio.output (18, False)  #让左电机不逆转
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    left=gpio.PWM(38,20)
    right=gpio.PWM(40,20)
    left.start(speed)
    right.start(speed)
    time.sleep(t)
    gpio.cleanup()

def pivot_turn_left(speed,t):
    atexit.register(gpio.cleanup)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, True)  #让右电机不逆转
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    left=gpio.PWM(38,20)
    right=gpio.PWM(40,20)
    left.start(speed)
    right.start(speed)
    time.sleep(t)
    gpio.cleanup()

def breaking(t):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    gpio.output(38,True)
    gpio.output(40,True)  
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  
    gpio.output(7,True)
    time.sleep(t)
    gpio.cleanup()
    
def stop(t):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    gpio.output(38,True)
    gpio.output(40,True)  
    gpio.output (12, False)  #让左电机不逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)
    gpio.cleanup()

pygame.init()  #pygame窗口初始化
screen = pygame.display.set_mode([320,240])
background = pygame.Surface(screen.get_size())
background.fill ([0,0,0])
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)

while True:  #创建一个无限循环
    for event in pygame.event.get():  #当接收到一个事件时
        if event.type == pygame.QUIT:  #如果这个事件是按下叉叉
            sys.exit()  #退出程序
        elif event.type == pygame.KEYDOWN:  #如果这个事件是按下某个按键
            if event.key ==pygame.K_q:  #如果这个按键是W
                forward(20,1)
                breaking(0.05)
                stop(1)            
                forward(40,1)
                breaking(0.05)
                stop(2)
                angle0=bearing()
                turn_right_angle(angle0,90)
                forward(100,1)
                breaking(0.05)
                stop(2)
            

                




