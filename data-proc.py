import numpy as np
import matplotlib.pyplot as plt

data_arr = np.loadtxt('data.txt', dtype = int)
with open('settings.txt', 'r') as s:
    tex = s.read()
    dur_t, freq_t, st_t, _ = tex.split('\n')
    dur = float(list(dur_t.split())[-1])
    freq = float(list(freq_t.split())[-1])
    st = float(list(st_t.split())[-1])

volt = data_arr * st
per = 1 / freq
t = np.arange(0, dur, per)
ch_time = np.argmax(volt) * per
disch_time = dur - ch_time

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)

ax.plot(t, volt, label = 'V(t)', color = 'red')

ax.set(title = ('Зависимость напряжения на конденсаторе от времени'), 
       xlabel = ('Время, с'), ylabel = ('Напряжение, В'),
       xlim = (0, dur), ylim = (0, 3.5) )

ax.text(50, 2.5, 'Время зарядки: {:.2f} c'.format(ch_time), bbox=dict(facecolor='blue', alpha=0.5))
ax.text(50, 2, 'Время разрядки: {:.2f} c'.format(disch_time), bbox=dict(facecolor='blue', alpha=0.5))

ax.minorticks_on()

ax.grid(which='major', linewidth = 2)
ax.grid(which='minor', linestyle = ':')

ax.legend()

fig.savefig('graph.svg')
plt.show()
