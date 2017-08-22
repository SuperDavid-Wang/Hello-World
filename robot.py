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
    gpio.output (38, True)
    gpio.output (40, True)
    gpio.setup(15,gpio.IN)
    gpio.setup(33,gpio.IN)
    gpio.setup(35,gpio.IN)
    gpio.setup(36,gpio.IN)
    gpio.setup(37,gpio.IN)
    gpio.setwarnings(False)

def  stop(t):
    init()
    gpio.output (12, False)  #让左电机不逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

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

def output_ultrasonic_wave():
    init()
    gpio.output(13,True)
    time.sleep(0.00001)
    gpio.output(13,False)
    while gpio.input(15) == False:
        pass
    t1 = time.time()
    gpio.cleanup()
    return t1

def distance():
    init()
    gpio.setwarnings(False)   
    t1 = output_ultrasonic_wave()
    init()
    gpio.setwarnings(False)
    while gpio.input(15) == True:
        pass
    t2 = time.time()
    t  = t2 - t1
    distance = t * 34000 / 2
    gpio.cleanup()
    return distance

def auto_drive():
    v = 0
    while v < 100:
        forward(0.05)
        d = distance()
        if  d < 40:
            stop(1)
            backward(1)
            turn = random.randint(1, 2)
            if turn == 1:
                turn_left(1.5)
            else:
                turn_right(1.5)
        gpio.cleanup()
        v += 1

def line_following():
    for i in range(0, 10000):
        init()
        if gpio.input(37) == False and gpio.input(36) == False and gpio.input(35) == False and gpio.input(33) == False:
            forward(0.001)
        elif gpio.input(37) == True or gpio.input(36) == True or gpio.input(35)==True or gpio.input(33)==True : 
            stop(1)

        init()  
        while gpio.input(36) == True: 
            pivot_turn_right(0.1)
            init()
            if gpio.input(36) == False:
                break       
        while gpio.input(35)==True: 
            pivot_turn_right(0.2)
            init()
            if gpio.input(35) == False:
                break
        while gpio.input(37)==True:
            pivot_turn_left(0.1)
            init()
            if gpio.input(37) == False:
                break        
        while gpio.input(33) == True: 
            pivot_turn_left(0.2)
            init()
            if gpio.input(33) == False:
                break
    init()
    stop(3)

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

def main():
    gpio.setwarnings(False)
    for event in pygame.event.get():  #当接收到一个事件时
        if event.type == pygame.QUIT:  #如果这个事件是按下叉叉
            sys.exit()  #退出程序
        elif event.type == pygame.KEYDOWN:  #如果这个事件是按下某个按键
            if event.key ==pygame.K_w:  #如果这个按键是W
                forward(0.05)  #前进0.05秒
            elif event.key ==pygame.K_s:  #如果这个按键是S
                backward(0.05)  #后退0.05秒
            elif event.key ==pygame.K_a:  #如果这个按键是A
                pivot_turn_left(0.05)  #左转0.05秒
            elif event.key ==pygame.K_d:  #如果这个按键是D
                pivot_turn_right(0.05)  #右转0.05秒
            elif event.key ==pygame.K_b:
                stop(1)
                break
            elif event.key ==pygame.K_o:
                auto_drive()
            elif event.key ==pygame.K_l:
                line_following()
            elif event.key ==pygame.K_h:
                steer(1)
                
##获得百度语音识别的口令
def get_access_token():
    url = "https://openapi.baidu.com/oauth/2.0/token"
    grant_type = "client_credentials"        ##用户证书
    client_id = "sOiMX9spfA9aDsG5Xj9qeG6X"
    client_secret = "06c5580d762083e50cf27989e1ecd286"

    url = url + "?" + "grant_type=" + grant_type + "&" + "client_id=" + client_id + "&" + "client_secret=" + client_secret

    resp = urllib2.urlopen(url).read()
    data = json.loads(resp.decode("utf-8"))  ##json.loads将字符串转换为字典
    return data["access_token"]              ##字符串.decode方法将其他编码格式的字符串（如utf-8)转换为python使用的unicode格式

##获得百度wav语音文件转文本服务
def baidu_asr(data, uuid, token):            ##automatic speech recognition
    speech_data = base64.b64encode(data).decode("utf-8")
    speech_length = len(data)

    post_data = {
    "format" : "wav",
    "rate" : 16000,
    "channel" : 1,
    "cuid" : uuid,
    "token" : token,
    "speech" : speech_data,
    "len" : speech_length
    }

    url = "http://vop.baidu.com/server_api"
    json_data = json.dumps(post_data).encode("utf-8")  ##json.dumps将字典转换为字符串，encode方法将unicode字符编码为其他格式（如utf-8)
    json_length = len(json_data)
    req = urllib2.Request(url,data = json_data)
    req.add_header("Content-Type", "application/json")
    req.add_header("Content-Length", json_length)

##    print("asr start \n")
    resp = urllib2.urlopen(req)
##    print("asr finish \n")
    resp = resp.read()
    resp_data = json.loads(resp.decode("utf-8"))
    if resp_data["err_no"] == 0:
        return resp_data["result"]   ##获得转换成功后的文本
    else:
##        print(resp_data)
        
        return "休息".decode("utf-8")   ##转换失败后返回的提示文本
    
##百度语音转文本主程序
def asr_main(filename):
    f = open(filename, "rb")     ##打开wav音频文件，open方法的参数r表示读取数据，b表示二进制数据
    audio_data = f.read()        ##读取wav音频文件的（二进制）数据
    f.close()
    token = get_access_token()
    uuid = "9589589"
    resp = baidu_asr(audio_data, uuid, token)
##    print(resp[0])
    return resp[0]




##上传文本给百度图灵机器人，并获得回答的文本
def result(word):
    reload(sys) 
    sys.setdefaultencoding('utf-8') 
    API_KEY = '89baa800ecaa4b728692ca869cc89e46'
    raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY
    queryStr = word
    TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
    req = urllib2.Request(url=TULINURL)
    result = urllib2.urlopen(req).read()
    hjson=json.loads(result)
    length=len(hjson.keys())
    content=hjson['text']

    if length==3:
        return content+hjson['url']
    elif length==2:
        return content
        
##获得百度文本转语音服务
def baidu_tts_by_post(data, uuid, token):
    post_data = {
    "tex" : data,
    "lan" : "zh",
    "cuid" : uuid,
    "ctp" : 1,
    "tok" : token,
    }

    url = "http://tsn.baidu.com/text2audio"
    post_data = urllib.urlencode(post_data).encode('utf-8')
    req = urllib2.Request(url, data = post_data)
    resp = urllib2.urlopen(req)
    resp = resp.read()
    return resp
##百度文本转语音主程序
def tts_main(filename, words):
    token = get_access_token()
    text = urllib.quote(words)
    uuid = "9589589"
    resp = baidu_tts_by_post(text, uuid, token)
    f = open(filename, "wb")    ##open方法的参数w表示写入数据，b表示二进制数据
    f.write(resp)
    f.close()


os.system("mpg123 sys_sound.mp3")    ##播放机器人启动语音
word = asr_main("cat1.wav")          ##将pi目录下的cat1.wav音频通过百度语音转文本服务转化为文本
word2=word.encode("utf-8")           ##将unicode编码的文本转换为utf-8编码，以支持中文字符
while True:
    if "休" in word2:     ##机器人启动后，用户不说话时的处理方法
        os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")  ##用树莓派rasbian系统自带的arecord软件通过usb外接的麦克风录制3秒钟的音频储存到cat1文件中
        word = asr_main("cat1.wav")
        word2=word.encode("utf-8")
        if "波西" in word2:
            steer(2)  ##原地旋转一圈
            os.system("mpg123 提示语.mp3")
            os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")
            word = asr_main("cat1.wav")
            word2=word.encode("utf-8")
            if "聪明" in word2:
                pivot_turn_left(1)
                os.system("mpg123 谢谢夸奖.mp3")
            elif "介绍" in word2:
                os.system("mpg123 自我介绍.mp3")
            elif "前进" in word2:
                while not "停" in word2:
                    forward(1)
                    os.system("mpg123 前进.mp3")
                    os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")  ##用树莓派rasbian系统自带的arecord软件通过usb外接的麦克风录制3秒钟的音频储存到cat1文件中
                    word = asr_main("cat1.wav")
                    word2=word.encode("utf-8")
                    if "停" in word2:
                        stop(1)
                        os.system("mpg123 提示语.mp3")
                    else:
                        pass
            elif "后退" in word2:
                while not "停" in word2:
                    backward(1)
                    os.system("mpg123 后退.mp3")
                    os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")  ##用树莓派rasbian系统自带的arecord软件通过usb外接的麦克风录制3秒钟的音频储存到cat1文件中
                    word = asr_main("cat1.wav")
                    word2=word.encode("utf-8")
                    if "停" in word2:
                        stop(1)
                        os.system("mpg123 提示语.mp3")
                    else:
                        pass
            elif "右转" in word2:
                pivot_turn_right(1)
                os.system("mpg123 右转.mp3")
            elif "左转" in word2:
                pivot_turn_left(1)
                os.system("mpg123 左转.mp3")         
            else:
                text = result(word.encode("utf-8"))  ##根据用户的语音指令，从百度图灵机器人获得回答文本
            ##    print text
                tts_main("test1.mp3", str(text))   ##将图灵机器人返回的文本通过百度语音合成转换为mp3音频
                os.system("mpg123 test1.mp3")   ##播放pi目录下的test1音频文件
        else:   ##机器人启动后，如果用户一直不说"天行者"的处理方法
            os.system("mpg123 exit.mp3")
            while "休" in word2:
                os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")
                word = asr_main("cat1.wav")
                word2=word.encode("utf-8")
                
    else:    ##机器人启动后，如果cat1音频文件中有上次关机时遗留的声音的处理方法；以及机器人休息后用户说了”天行者“后的处理
        steer(1)
        os.system("mpg123 提示语.mp3")
        os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")
        word = asr_main("cat1.wav")
        word2=word.encode("utf-8")
        if "聪明" in word2:
            os.system("mpg123 谢谢夸奖.mp3")
        elif "介绍" in word2:
            os.system("mpg123 自我介绍.mp3")
        elif "前进" in word2:
            while not "停" in word2:
                forward(1)
                os.system("mpg123 前进.mp3")
                os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")  ##用树莓派rasbian系统自带的arecord软件通过usb外接的麦克风录制3秒钟的音频储存到cat1文件中
                word = asr_main("cat1.wav")
                word2=word.encode("utf-8")
                if "停" in word2:
                        stop(1)
                        os.system("mpg123 提示语.mp3")
                else:
                    pass
        elif "后退" in word2:
            while not "停" in word2:
                backward(1)
                os.system("mpg123 后退.mp3")
                os.system("arecord -D 'plughw:1' -d 3 -f S16_LE -r 16000 cat1.wav ")  ##用树莓派rasbian系统自带的arecord软件通过usb外接的麦克风录制3秒钟的音频储存到cat1文件中
                word = asr_main("cat1.wav")
                word2=word.encode("utf-8")
                if "停" in word2:
                        stop(1)
                        os.system("mpg123 提示语.mp3")
                else:
                    pass
        elif "右转" in word2:
            pivot_turn_right(1)
            os.system("mpg123 右转.mp3")
        elif "左转" in word2:
            pivot_turn_left(1)
            os.system("mpg123 左转.mp3")    
        else:
            text = result(word.encode("utf-8"))
        ##    print text
            tts_main("test1.mp3", str(text))
            os.system("mpg123 test1.mp3")





        
    
    

