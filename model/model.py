import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import cv2
import os
from PIL import Image

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

x_train = ImageDataGenerator(rescale= 1/255)
x_test = ImageDataGenerator(rescale = 1/255)

train_gen = x_train.flow_from_directory(
    'E:/blockchain/Neighborhood Hacks/model/train',
    target_size = (150,112),
    batch_size = 100,
    class_mode= 'binary'
)

test_gen = x_test.flow_from_directory(
    'E:/blockchain/Neighborhood Hacks/model/test',
    target_size = (150,112),
    batch_size = 50,
    class_mode = 'binary'
)

model = tf.keras.models.Sequential([
    keras.layers.Conv2D(16, (3,3), activation = 'relu', input_shape = (150,112, 3)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(32, (3,3), activation = 'relu'),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(64, (3,3), activation = 'relu'),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation = 'relu'),
    keras.layers.Dense(1, activation = 'sigmoid')
])

model.summary()

model.compile(
    loss = 'binary_crossentropy',
    optimizer = RMSprop(learning_rate = 0.001),
    metrics = ['accuracy']
)

hist = model.fit_generator(
    train_gen,
    steps_per_epoch = 46,
    epochs = 3,
    validation_data= test_gen,
    validation_steps = 56
)

os.mkdir('saved model')
model.save('saved model/myModel')