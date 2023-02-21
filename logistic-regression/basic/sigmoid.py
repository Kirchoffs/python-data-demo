import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6)
print(type(x))
y = 1.0 / (1.0 + np.exp(-x))
print(type(y))

plt.plot(x, y)
plt.show()
