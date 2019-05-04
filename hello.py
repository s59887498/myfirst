import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 50)
y1 = 2*x + 1

y2 = x**2

plt.figure()

plt.subplot(2,2,2)
plt.plot(x, y2,'ro',label='87')
plt.xlabel('time')
plt.ylabel('temp')
plt.legend(loc=1)

plt.subplot(2,2,4)
plt.plot(x,y1,color='green',label='ggininder')
plt.xlabel('time')
plt.ylabel('temp')

plt.legend(loc=1)
plt.show()