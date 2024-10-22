import matplotlib.pyplot as plt
import numpy as np

with open('settings.txt', 'r') as settings:
    tmp=[float(i) for i in settings.read().split('\n')]
data=np.loadtxt('7.1-data.txt', dtype=int)
vol=[i*tmp[0] for i in data]
time_step=np.array(tmp[1]*np.arange(1, len(vol)+1,1))
max_vol=0.0
max_index=0
for i in range(len(vol)):
    if(max_vol<vol[i]):
        max_vol=vol[i]
        max_index=i

fig, ax=plt.subplots(figsize=(6,6))
ax.plot(time_step, vol, label='V(t)', marker='o', markevery=5)
plt.grid()
plt.minorticks_on()
plt.grid(b=True, which='major', color='grey')
plt.grid(b=True, which='minor', color='0.8')
plt.xlim(0, 10)
plt.legend()
t=round(time_step[max_index], 2)
ax.text(4, 1.5, 'время заряда конденсатора ={}'.format(t), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})

plt.title('Процесс зарядки и разрядки конденсатора в RC-цепочке')
plt.ylabel('Напряжение, В')
plt.xlabel('Время, с')
# fig = plt.figure(figsize=(16,10), dpi=600)
plt.savefig("v_t.svg")
plt.show()



