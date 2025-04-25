# Elliot Mayer

import tensorflow as tf

# Load the data
mnist = tf.keras.datasets.mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]
X_train, X_valid, X_test = X_train / 255., X_valid / 255., X_test / 255.

# Set the random number seed
tf.random.set_seed(42)

# Define the model
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(300, activation="relu"))
# model.add(tf.keras.layers.Dense(100, activation="relu"))
# model.add(tf.keras.layers.Dense(10, activation="softmax"))

# Set the random number seed
tf.random.set_seed(42)

#resize, the -1 matches to the origional size
X_train = X_train.reshape(-1, 28, 28, 1)
X_valid = X_valid.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28, 1]))


model.add(tf.keras.layers.Conv2D(32, 3, activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Conv2D(64, 3,  activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Conv2D(128, 3, activation='relu'))

model.add(tf.keras.layers.Flatten())
# trying an additional dense layer
model.add(tf.keras.layers.Dense(128 , activation="relu"))

model.add(tf.keras.layers.Dropout(0.3)) #apparently prevents overfitting
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.summary()


# Compile the model
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

# Train the model
# TODO You may be able to turn down the number of epochs
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_valid, y_valid))

# Evaluate the model on test data
# TODO Uncomment this, but only once you are sure you have your final model!
model.evaluate(X_test, y_test)

# Plot the learning curve
import matplotlib.pyplot as plt
import pandas as pd

pd.DataFrame(history.history).plot(
    figsize=(8, 5), xlim=[0, 29], ylim=[0, 1], grid=True, xlabel="Epoch",
    style=["r--", "r--.", "b-", "b-*"])
plt.legend(loc="lower left")  # extra code
plt.show()