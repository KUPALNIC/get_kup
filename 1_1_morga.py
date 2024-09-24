import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setup(23, gp.OUT)
gp.setup(16, gp.IN)
while True:
    if gp.input(16):
        gp.output(23, 1)
    else:
        gp.output(23, 0)




