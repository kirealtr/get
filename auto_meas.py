import matplotlib.pyplot as plt
meas = [i**3 for i in range(20)]
plt.plot(meas)
str_meas = list(map(str, meas))

with open('data.txt', 'w') as outp:
    outp.write('\n'.join(str_meas))

plt.show()