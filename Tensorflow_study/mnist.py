import tensorflow as tf

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

import numpy as np
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt

plt.imshow(training_images[0])
print(training_images[0])
print(training_labels[0])

training_images = training_images/255.0
training_labels = training_labels/255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(64, activation=tf.nn.softmax)
    ]
)

model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

model.fit(training_images,training_labels,epochs=5)

model.evaluate(test_images,test_labels)

classifications = model.predict(test_images)
print(classifications[0])

print(test_labels[0])
