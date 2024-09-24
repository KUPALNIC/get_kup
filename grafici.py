import RPi.GPIO as gp
import time 
import random
import numpy as np
import matplotlib.pyplot as plt
import threading as tr
gp.setmode(gp.BCM)
dac =[8,11,7,1,0,5,12,6]
gp.setup(dac, gp.OUT)
T=1

def binary(n):
    sg=[]
    while n!=0:
        sg.append(n%2)
        n=n//2
    
    while len(sg) < 8:
        sg.append(0)
    sg.reverse()
    return sg

def vivod():
    global T
    while True:
        # x=np.linspace(0, input("T= "))
        for i in range(0, 256, 1):
            gp.output(dac, binary(int(i)))
            time.sleep(T/511)
        for i in range(255, 0, -1):
            gp.output(dac, binary(int(i)))
            time.sleep(T/511)

tr.Thread(target=vivod).start()

try:
    T =int(input("T= "))
    input()
except:
    pass
finally:
    gp.output(dac, [0,0,0,0,0,0,0,0])
    gp.cleanup()
