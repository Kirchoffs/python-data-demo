# Estimate

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data('mnist.npz')
X_test = x_test.reshape(10000, 784)
X_test = X_test.astype('float32')
X_test /= 255

from keras.utils import to_categorical
n_classes = 10
Y_test = to_categorical(y_test, n_classes)

from keras.models import load_model

save_dir = "./mnist/model/"
model_name = 'keras_mnist.h5'
import os
model_path = os.path.join(save_dir, model_name)

mnist_model = load_model(model_path)

loss_and_metrics = mnist_model.evaluate(X_test, Y_test, verbose = 2)
    
print("Test Loss: {}".format(loss_and_metrics[0]))
print("Test Accuracy: {}%".format(loss_and_metrics[1] * 100))

import numpy as np

predicted_classes = mnist_model.predict(X_test)
predicted_classes = np.argmax(predicted_classes, axis = 1)

correct_indices = np.nonzero(predicted_classes == y_test)[0]
incorrect_indices = np.nonzero(predicted_classes != y_test)[0]
print("Classified correctly count: {}".format(len(correct_indices)))
print("Classified incorrectly count: {}".format(len(incorrect_indices)))
