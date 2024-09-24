import RPi.GPIO as gp
import time 
import random
import numpy as np
import matplotlib.pyplot as plt
gp.setmode(gp.BCM)
dac = [6,12,5,0,1,7,11,8]
dac.reverse()
gp.setup(dac, gp.OUT)
# for i in range(0, 8):
#     number.append(random.randint(0, 1))
def binary(n):
    num=[]
    while n!=0:
        num.append(n%2)
        n=n//2
    
    while len(num) < 8:
        num.append(0)
    num.reverse()
    return num
# print(binary(int(input())))

pattern = binary(int(input()))
print(pattern)
gp.output(dac, pattern)
time.sleep(10)
gp.output(dac, 0)
gp.cleanup()

# x=[0, 5, 32, 64, 127, 255]
# y=[]
# plt.plot(x, y)