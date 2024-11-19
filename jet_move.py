import spidev
import time
import RPi.GPIO as GPIO

global f 
f = open('90mm.txt', 'w')
'''
'''
def write_to_f(n):
    f.write(str(n)+'\n')
    print(n)



########################################
#   Open, use and close SPI ADC
########################################

########################################
# Do not forget to setup GPIO pins to SPI functions!
#
# Enter the followig commands into RPi terminal:
#
# raspi-gpio get
# raspi-gpio set 9 a0
# raspi-gpio set 10 a0
# raspi-gpio set 11 a0
# raspi-gpio get
########################################

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC has been initialized")

def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1


########################################
#   Setup and use GPIO for step motor
########################################

directionPin = 27
enablePin = 22
stepPin = 17

def initStepMotorGpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([directionPin, enablePin, stepPin], GPIO.OUT)
    print ("GPIO for step motor have been initialized")

def deinitStepMotorGpio():
    GPIO.output([directionPin, enablePin, stepPin], 0)
    GPIO.cleanup()
    print ("GPIO cleanup finished")

def step():
    GPIO.output(stepPin, 0)
    time.sleep(0.005)
    GPIO.output(stepPin, 1)
    time.sleep(0.005)
    
def stepForward(n):
    GPIO.output(directionPin, 1)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()
        write_to_f(getAdc()) 

    GPIO.output(enablePin, 0)

def stepBackward(n):
    GPIO.output(directionPin, 0)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()
        write_to_f(getAdc()) 

    GPIO.output(enablePin, 0)


########################################
# Run this script, enter h for help
# and moove the Pitot tube manually.
########################################

try:
    steps = 0

    initStepMotorGpio()
    initSpiAdc()
    while True:
        n = input('Enter steps or command (h - help) > ')

        if n == 'h':
            print('\nHelp for "Jet Mover":')
            print('     50 - positive integer to step forward')
            print('    -80 - negative integer to step backward')
            print('      s - actual position relative to zero')
            print('      z - set zero')
            print('      q - exit')
            print('Try in now!\n')

        elif n == 's':
            print(steps, ' steps')

        elif n == 'z':
            steps = 0
            print(steps, ' steps')

        elif n == 'q':
            print(steps, ' steps')
            break

        else:
            n = int(n)
            if n < 0:
                stepBackward(abs(n))
            if n > 0:
                stepForward(n)
            
            steps += n
        
              


finally:
    deinitStepMotorGpio()