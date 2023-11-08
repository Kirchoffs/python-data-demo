import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
y_upper = 1.0 * np.ones(len(x))
y_lower = 0.0 * np.ones(len(x))
plt.plot(x, y)
plt.plot(x, y_upper, linestyle = "--")
plt.plot(x, y_lower, linestyle = "--")
plt.ylim(-0.1, 1.1)
plt.show()
