# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio
import  time
import  sys
from compass import *

def init():  #定义初始化GPIO引脚的函数
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.IN)
    gpio.setup(33,gpio.IN)
    gpio.setup(35,gpio.IN)
    gpio.setup(36,gpio.IN)
    gpio.setup(37,gpio.IN)
    gpio.setup(38,gpio.OUT)
    gpio.setup(40,gpio.OUT)
    gpio.output(38, True)
    gpio.output(40, True)
##    left=gpio.PWM(38,20)
##    right=gpio.PWM(40,20)
##    left.start(100)
##    right.start(100)

def forward(t):  #定义前进的函数
    init()  #初始化引脚
    gpio.output (12, True)  #让右电机逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def backward(t):  #定义后退的函数
    init()  #初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  
    gpio.output(7,True)
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def turn_right(t):  #定义右转的函数
    init()  #初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机 顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def turn_left(t):  #定义左转的函数
    init()  #初始化引脚
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出


def pivot_turn_right(t):  #定义右转的函数
    init()  #初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机不顺转
    gpio.output (22, True)  #让左电机 顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def pivot_turn_left(t):  #定义左转的函数
    init()  #初始化引脚
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, True)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    
def  stop(t):
    init()
    gpio.output (12, False)  #让左电机不逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def turn_angle_180(angle0, angle1):   #if turning angle<180, the function can calculate the correct angle
    if angle0<=0:                                       #angle0=bearing(), angle1=bearing()
        angle0+=2*math.pi
    else:
        pass
    degree0 = math.degrees(angle0)
    if angle1<=0:
        angle1+=2*math.pi
    else:
        pass
    degree1=math.degrees(angle1)
    if degree1>=degree0:
        turn_degree = degree1 - degree0
        if turn_degree<=180:
            turn_degree = turn_degree
        else:
            turn_degree = degree0-degree1+360 
    else:
        turn_degree = degree1-degree0+360
        if turn_degree<=180:
            turn_degree = turn_degree
        else:
            turn_degree = degree0-degree1
    return turn_degree

def angle_right(angle0, angle1):   #if turning right, the function can calculate the correct angle
    if angle0<=0:                                     
        angle0+=2*math.pi
    else:
        pass
    degree0 = math.degrees(angle0)
    if angle1<=0:
        angle1+=2*math.pi
    else:
        pass
    degree1=math.degrees(angle1)
    if degree1>=degree0:
        turn_degree = degree1 - degree0
    else:
        turn_degree = degree1-degree0+360
    return turn_degree

def angle_left(angle0, angle1):   #if turning left, the function can calculate the correct angle
    if angle0<=0:                                     
        angle0+=2*math.pi
    else:
        pass
    degree0 = math.degrees(angle0)
    if angle1<=0:
        angle1+=2*math.pi
    else:
        pass
    degree1=math.degrees(angle1)
    if degree0>=degree1:
        turn_degree = degree0 - degree1
    else:
        turn_degree = degree0-degree1+360 
    return turn_degree


def turn_right_angle(angle0, angle):
    time.sleep(1)
    turn_degree = 0
    pivot_turn_right(0.3)
    while abs(turn_degree-angle)>=1:
        init()
        if turn_degree <= angle :
            pivot_turn_right(0.005)
            angle1 = bearing()
            turn_degree=angle_right(angle0, angle1)
        else:
            pivot_turn_left(0.005)
            angle1 = bearing()
            turn_degree=angle_right(angle0, angle1)
    stop(1)
    gpio.cleanup()


def turn_left_angle(angle0, angle):
    time.sleep(1)
    turn_degree = 0
    pivot_turn_left(0.2)
    while abs(turn_degree-angle)>=1:
        if turn_degree <= angle:
            pivot_turn_left(0.005)
            angle1 = bearing()
            turn_degree=angle_left(angle0, angle1)
        else:
            pivot_turn_right(0.005)
            angle1 = bearing()
            turn_degree=angle_left(angle0, angle1)
    stop(1)
    gpio.cleanup()



##
##angle0 =bearing()    #set the initial angle
##forward(2)
##stop(2)
##turn_right_angle(angle0, 90)    #turn right for 90 from the initial angle
##stop(1)
##forward(1)
##stop(2)
##turn_right_angle(angle0, 180)
##stop(1)
##forward(2)
##stop(2)
##turn_right_angle(angle0, 270)
##stop(1)
##forward(1)
##stop(2)
##angle1=bearing
##turn_right_angle(angle1, 90)
##stop(5)







##for i in range(5):
##    angle0= bearing()
##    print "right"
##    time.sleep(5)
##    angle1=bearing()
##    print angle_right(angle0, angle1)
##for i in range(5):
##    print "left"
##    angle0= bearing()
##    time.sleep(10)
##    angle1=bearing()
##    print angle_left(angle0, angle1)

