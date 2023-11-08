import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = np.maximum(x, 0)
plt.plot(x, y)
plt.show()
