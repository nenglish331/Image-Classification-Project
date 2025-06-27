import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

iteration = 11
input_shape = (640, 360, 3)
num_classes = 10
batch_size = 4
epochs = 12

# Create an ImageDataGenerator for data augmentation and preprocessing
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    # rotation_range=20,
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    # shear_range=0.2,
    # zoom_range=0.2,
    # horizontal_flip=True
)

# Load the training data from the image folder
train_generator = datagen.flow_from_directory(
    './images/train',
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='categorical',
)

# Create a CNN model
model = Sequential()

# Add Convolutional layers
model.add(Conv2D(32, (5, 5), activation='relu', padding='same', input_shape=input_shape))
model.add(MaxPooling2D((2, 2)))  

model.add(Conv2D(64, (10, 10), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2)))  

model.add(Conv2D(128, (10, 10), activation='relu', padding='same'))  
model.add(MaxPooling2D((2, 2))) 

# model.add(Conv2D(256, (5, 5), activation='elu', padding='same')) 
# model.add(MaxPooling2D((2, 2)))

# model.add(Conv2D(512, (5, 5), activation='elu', padding='same')) 
# model.add(MaxPooling2D((2, 2)))

# Flatten the output
model.add(Flatten())

# Add Dense layers
model.add(Dense(128, activation='relu'))  # Number of neurons: 128
# model.add(Dropout(0.25))  # Dropout rate
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',  # Learning rate: Default value for Adam optimizer
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_generator,
          steps_per_epoch=train_generator.samples // batch_size,
          epochs=epochs)

# Save the trained model
model.save(f'./models/trained_model_{iteration}.keras')