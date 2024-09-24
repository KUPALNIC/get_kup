import RPi.GPIO as gp
import time as tm 
gp.setmode(gp.BCM)
leds=[2,3,4,17,27,22,10,9]
# number=[0,1]
gp.setup(leds, gp.OUT)
for i in range(3):
    for j in leds:
        gp.output(j, gp.HIGH)
        tm.sleep(0.2)
        gp.output(j, gp.LOW)
gp.cleanup()
