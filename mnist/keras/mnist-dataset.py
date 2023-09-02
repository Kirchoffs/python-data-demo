from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data('mnist.npz') # Download data to ~/.keras/datasets/mnist.npz
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 5, figsize = (10, 6))
fig.tight_layout()
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap = 'Greys')
    ax.set_title("Label: {}".format(y_train[i]))
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()