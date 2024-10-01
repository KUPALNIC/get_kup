import RPi.GPIO as gp
import time 
import random
import numpy as np
import matplotlib.pyplot as plt
import threading as tr
gp.setmode(gp.BCM)
dac =[8,11,7,1,0,5,12,6]
gp.setup(dac, gp.OUT)
comp=14
tr =13
gp.setup(tr, gp.OUT, initial=1)
gp.setup(comp, gp.IN)

def binary(n):
    sg=[]
    while n!=0:
        sg.append(n%2)
        n=n//2
    
    while len(sg) < 8:
        sg.append(0)
    sg.reverse()
    return sg

def adc():
    for i in range(256):
        gp.output(dac, binary(int(i)))
        time.sleep(0.001)
        if gp.input(comp)==1:
            return i
        
    
try:
    while 1:
        print(adc()*3.3/256)
        
finally:
    gp.output(dac, [0,0,0,0,0,0,0,0])
    gp.cleanup()
