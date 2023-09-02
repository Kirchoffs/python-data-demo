from keras.datasets import mnist

# Get data

(x_train, y_train), (x_test, y_test) = mnist.load_data('mnist.npz')

print(x_train.shape, type(x_train))
print(y_train.shape, type(y_train))

# Reshape data

X_train = x_train.reshape(60000, 784)
X_test = x_test.reshape(10000, 784)
print(X_train.shape, type(X_train))
print(X_test.shape, type(X_test))

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# Normalize data

X_train /= 255
X_test /= 255

# Display data distribution

import numpy as np
import matplotlib.pyplot as plt

label, count = np.unique(y_train, return_counts = True)
print(label, count)

fig = plt.figure()
plt.bar(label, count, width = 0.7, align = 'center')
plt.title("Label Distribution")
plt.xlabel("Label")
plt.ylabel("Count")
plt.xticks(label)
plt.ylim(0, 7500)

for a, b in zip(label, count):
    plt.text(a, b, '%d' % b, ha = 'center', va = 'bottom',fontsize = 10)

plt.show()

# One-hot encoding

from keras.utils import to_categorical

n_classes = 10

print("Shape before one-hot encoding: ", y_train.shape)
Y_train = to_categorical(y_train, n_classes)
print("Shape after one-hot encoding: ", Y_train.shape)
print(y_train[0], Y_train[0])

Y_test = to_categorical(y_test, n_classes)

# Build model

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()

model.add(Dense(512, input_shape = (784, )))
model.add(Activation('relu'))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'], optimizer = 'adam')

history = model.fit(X_train, Y_train, batch_size = 128, epochs = 5, verbose = 2, validation_data = (X_test, Y_test))

fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc = 'lower right')

plt.subplot(2,1,2)
plt.plot(history.history['loss'])      
plt.plot(history.history['val_loss']) 
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc = 'upper right')
plt.tight_layout()

plt.show()

# Save model

import os

save_dir = "./mnist/model/"

if os.path.exists(save_dir):
    import shutil
    shutil.rmtree(save_dir)

os.makedirs(save_dir)

model_name = 'keras_mnist.h5'
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)

# Load model

from keras.models import load_model

mnist_model = load_model(model_path)