# My solution to weekly task 02
# Author: Tosin Araba

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 4))
ypoints = xpoints
ypoints = xpoints * xpoints
ypoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints, label='f')
plt.plot(xpoints, ypoints, label ='g')
plt.plot(xpoints, ypoints, label ='h')
plt.show()
