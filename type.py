#!/usr/bin/python

import os, time


x = "Welcome to the Matrix!"
y = 0
while y <=  len(x):
    os.system("clear")
    print(x[:y])
    time.sleep(.2)
    y +=1
