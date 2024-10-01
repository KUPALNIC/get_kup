import RPi.GPIO as gp
import time 
# import random
# import numpy as np
# import matplotlib.pyplot as plt
# import threading as tr
gp.setmode(gp.BCM)
dac =[8,11,7,1,0,5,12,6]
led=[2,3,4,17,27,22,10,9]
gp.setup(led, gp.OUT)
gp.setup(dac, gp.OUT)
gp.output(led, [0,0,0,0,0,0,0,0])
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
    c=0
    for i in range(7, -1, -1):
        
        gp.output(dac, binary(c+2**i))
        time.sleep(0.001)
        if gp.input(comp)==0:
            c+=2**i
    return c

try:
    while 1:
        leds=[0,0,0,0,0,0,0,0]
        
        index=0
        if adc()==0:
            gp.output(led, leds)
        else:
            ost=adc()//32+1
            for i in range(ost):
                leds[i]=1
        gp.output(led,leds)
        print(float(adc())*3.3/256)
        
        
finally:
    gp.output(dac, [0,0,0,0,0,0,0,0])
    gp.cleanup()
