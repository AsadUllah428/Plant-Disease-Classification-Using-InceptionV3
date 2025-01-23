# -*- coding: utf-8 -*-
"""GitHub Files.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xKuf5-nv4iRVOdnK7Nf-Zcsy_9b0EdZc
"""

#First we create a API from out kaggle account
#Than we will upload and use that .json to connect our kaggle account
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Replace 'noulam/tomato' with the dataset's name from Kaggle
!kaggle datasets download -d noulam/tomato

#Extracting the zip file
import zipfile
with zipfile.ZipFile("tomato.zip", 'r') as zip_ref:
    zip_ref.extractall("data")

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# import the libraries as shown below

from tensorflow.keras.layers import Input, Lambda, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
#from keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

# re-size all the images to this
IMAGE_SIZE = [224, 224]

train_path = '/content/data/New Plant Diseases Dataset(Augmented)/train'
valid_path = '/content/data/New Plant Diseases Dataset(Augmented)/valid'

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.models import Model

# Use pre-trained InceptionV3 without the top layer
inception = InceptionV3(input_shape=[224, 224, 3], weights='imagenet', include_top=False)

# Freeze the pre-trained layers
for layer in inception.layers:
    layer.trainable = False

# Flatten the output layer and add a Dense layer for predictions
x = Flatten()(inception.output)
prediction = Dense(10, activation='softmax')(x)  # 10 classes

# Create the model
model = Model(inputs=inception.input, outputs=prediction)

# Compile the model
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# view the structure of the model
model.summary()

# Use the Image Data Generator to import the images from the dataset
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
#Here we will just rescale our test data as testing has to be done on it
test_datagen = ImageDataGenerator(rescale = 1./255)

# Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory('/content/data/New Plant Diseases Dataset(Augmented)/train',
                                                 target_size = (224, 224),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('/content/data/New Plant Diseases Dataset(Augmented)/valid',
                                            target_size = (224, 224),
                                            batch_size = 16,
                                            class_mode = 'categorical')

# fit the model
# Run the cell. It will take some time to execute
Results = model.fit(
  training_set,
  validation_data=test_set,
  epochs=10,
  steps_per_epoch=len(training_set),
  validation_steps=len(test_set)
)

# plot the loss
plt.plot(r.history['loss'], label='train loss')
plt.plot(r.history['val_loss'], label='val loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')

# plot the accuracy
plt.plot(r.history['accuracy'], label='train acc')
plt.plot(r.history['val_accuracy'], label='val acc')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')




