import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
def left(tf): 
    GPIO.output(29, False)
    GPIO.output(37, False)
    GPIO.output(13, False)
    GPIO.output(31, False)
    motorl = GPIO.PWM(33, 50)
    motorr = GPIO.PWM(32, 50)
    motorr.start(0)
    motorl.start(0)
    motorl.ChangeDutyCycle(25)
    motorr.ChangeDutyCycle(25)
    time.sleep(tf)
    GPIO.cleanup((32, 31, 33))

def right(tf): 
    GPIO.output(29, False)
    GPIO.output(37, True)
    GPIO.output(13, True)
    GPIO.output(31, False)
    motorr = GPIO.PWM(32, 50)
    motorr.start(0)
    motorl = GPIO.PWM(33, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(25)
    motorr.ChangeDutyCycle(25)
    time.sleep(tf)
    GPIO.cleanup((32, 31, 33))

def forward(tf): 
    GPIO.output(37, True)
    GPIO.output(13, False)
    GPIO.output(29, False)
    GPIO.output(31, False)
    motorr = GPIO.PWM(32, 50)
    motorl = GPIO.PWM(33, 50)
    motorl.start(0)
    motorr.start(0)
    motorr.ChangeDutyCycle(20)
    motorl.ChangeDutyCycle(20)
    time.sleep(tf)
    GPIO.cleanup((32, 33))

def reverse(tf): 
    GPIO.output(29, False)
    GPIO.output(31, False)
    GPIO.output(13, True)
    GPIO.output(37, False)
    motorr = GPIO.PWM(32, 50)
    motorl = GPIO.PWM(33, 50)
    motorl.start(0)
    motorr.start(0)
    motorr.ChangeDutyCycle(20)
    motorl.ChangeDutyCycle(20)
    time.sleep(tf)
    GPIO.cleanup((32, 33))

def brake(tf): 
    GPIO.output(29, True)
    GPIO.output(31, True)
    time.sleep(tf)

def lamp(tf):
    GPIO.output(15, True)
    time.sleep(tf)

def key_input(event):
    init()
    print 'Key:' , event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)
    elif key_press.lower() == 'b':
        brake(sleep_time)
    elif key_press.lower() == 'l':
        lamp(sleep_time)
    elif key_press.lower() == 'k':
        GPIO.output(15, False)


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
    











