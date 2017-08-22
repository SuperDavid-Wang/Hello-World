# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio    #导入所有模块
import  time
import  sys
import pygame

gpio.setwarnings(False)
pygame.init()  #pygame窗口初始化
screen = pygame.display.set_mode([320,240])
background = pygame.Surface(screen.get_size())
background.fill ([0,0,0])
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)

def init():  #定义初始化GPIO引脚的函数
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    left=gpio.PWM(38,20)
    right=gpio.PWM(40,20)
    left.start(0)
    right.start(0)
    left.ChangeDutyCycle(30)
    right.ChangeDutyCycle(30)
    gpio.setup(15,gpio.IN)
    

def forward(t):  #定义前进的函数
    init()#初始化引脚
    gpio.output (12, True)  #让右电机逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)

def backward(t):  #定义后退的函数
    init()#初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  
    gpio.output(7,True)
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)
    
def turn_right(t):  #定义右转的函数
    init()#初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机 顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)

def turn_left(t):  #定义左转的函数
    init()#初始化引脚
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)

while True:  #创建一个无限循环
    for event in pygame.event.get():  #当接收到一个事件时
        if event.type == pygame.QUIT:  #如果这个事件是按下叉叉
            sys.exit()  #退出程序
        elif event.type == pygame.KEYDOWN:  #如果这个事件是按下某个按键
            if event.key ==pygame.K_w:  #如果这个按键是W
                forward(0.05)  #前进0.05秒
            elif event.key ==pygame.K_s:  #如果这个按键是S
                backward(0.05)  #后退0.05秒
            elif event.key ==pygame.K_a:  #如果这个按键是A
                turn_left(0.05)  #左转0.05秒
            elif event.key ==pygame.K_d:  #如果这个按键是D
                turn_right(0.05)  #右转0.05秒

