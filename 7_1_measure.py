import RPi.GPIO as gp
import time 
import matplotlib.pyplot as plt
gp.setmode(gp.BCM)
dac =[8,11,7,1,0,5,12,6]
led=[2,3,4,17,27,22,10,9]
gp.setup(led, gp.OUT)
gp.setup(dac, gp.OUT)
gp.output(led, [0,0,0,0,0,0,0,0])
comp = 14
tr = 13
gp.setup(tr, gp.OUT, initial=0)
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
        time.sleep(0.005)
        if gp.input(comp)==0:
            c+=2**i
    return c

def to_leds(a):
        leds=[0,0,0,0,0,0,0,0]
        index=0
        if adc()==0:
            gp.output(led, leds)
        else:
            ost=adc()//32+1
            for i in range(ost):
                leds[i]=1
        gp.output(led,leds)


a = 0
x = []
start = time.time()
gp.output(tr, gp.HIGH)
while a < 207:
    a = adc()
    x.append(a)
    to_leds(a)
    print(a)
    

gp.output(tr, gp.LOW)
while a > 193:
    a = adc()
    x.append(a)
    to_leds(a)
    print(a)
end = time.time()
t = (end-start)/len(x)
x_t=[]
for i in range(1,len(x)+1,1):
    x_t.append(t*i)
fig, ax = plt.subplots()
ax.plot(x_t, x)


f = open('data.txt','w')
f1= open('settings.txt', 'w')
f1.write('0.013 ' + '\n')
f1.write(str(t))
for i in range(len(x)):
    f.write(str(x[i]) + '\n')
f.close()
f1.close()

print('--------')
print('Время:',end-start)
print("Период:",t)
print("Частота:",1/t)
print("Шаг квантования:",3.3/256)

gp.output(dac, [0,0,0,0,0,0,0,0])
gp.output(led, [0,0,0,0,0,0,0,0])
gp.cleanup()
plt.xlabel("time, s")
plt.ylabel("voltage, u")
plt.title('V(t)')
plt.grid()
plt.show()
