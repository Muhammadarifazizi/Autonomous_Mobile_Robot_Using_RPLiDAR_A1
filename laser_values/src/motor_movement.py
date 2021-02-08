#!/usr/bin/env python3

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyUSB1')
# setup vaiable for motor DC pin
#m: motor   l:left      r:right    f:forward     b:backward     d:digital       p:PWM pin(3, 5, 6, 9, 10)
# incase of PWM pin, arduino accept value from 0 to 255 that represent value from 0 to 100%, 
# but in pyfrimata it make easier with provide value from 0 to 1  
mlf = board.get_pin('d:6:p')
mlb = board.get_pin('d:5:p')
mrf = board.get_pin('d:9:p')
mrb = board.get_pin('d:10:p')

def forward():
    mlf.write(1)
    mrf.write(1)
    mlb.write(0)
    mrb.write(0)

def backward():
    mlf.write(0)
    mrf.write(0)
    mlb.write(1)
    mrb.write(1)

def left():
    mlf.write(0)
    mrf.write(1)
    mlb.write(0)
    mrb.write(0)

def right():
    mlf.write(1)
    mrf.write(0)
    mlb.write(0)
    mrb.write(0)

def obliqueRightForward():
    mlf.write(1)
    mrf.write(0.5)
    mlb.write(0)
    mrb.write(0)

def obliqueLeftForward():
    mlf.write(0.5)
    mrf.write(1)
    mlb.write(0)
    mrb.write(0)

def obliqueRightBackward():
    mlf.write(0)
    mrf.write(0)
    mlb.write(1)
    mrb.write(0.5)

def obliqueLeftBackward():
    mlf.write(0)
    mrf.write(0)
    mlb.write(0.5)
    mrb.write(1)

def stop():
    mlf.write(0)
    mrf.write(0)
    mlb.write(0)
    mrb.write(0)

#while True:
#    move = input(' f/b/l/r  or  g/i/h/j : ')
#    if move == 'f':
#        forward()
#    elif move == 'b':
#        backward()
#    elif move == 'l':
#        left()
#    elif move == 'r':
#        right()
#    elif move == 'g':
#        obliqueRightForward()
#    elif move == 'i':
#        obliqueLeftForward()
#    elif move == 'h':
#        obliqueRightBackward()
#    elif move == 'j':
#        obliqueLeftBackward()
#    else:
#        stop()
#        break

