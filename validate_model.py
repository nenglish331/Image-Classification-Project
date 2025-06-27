import numpy as np
import tensorflow as tf

# Validate the model
# Load the saved model
iteration = 10
model_path = f'./models/trained_model_{iteration}.keras'
first_path = "C:/Users/nengl/Videos/Machine Learning Project/models/trained_model_1.keras"
model = tf.keras.models.load_model(model_path)
target = (640, 360)
batch_size = 4

# Set the path to your validation image folder
validation_image_folder = './images/validation'

# Create an ImageDataGenerator for preprocessing validation data
validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

# Load the validation data from the image folder
validation_generator = validation_datagen.flow_from_directory(
    validation_image_folder,
    target_size=target,  # Adjust the target size if necessary
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False  # Important: Do not shuffle the data
)

# Evaluate the model on the validation data
validation_loss, validation_accuracy = model.evaluate(validation_generator, verbose=1)
print("Validation Accuracy:", validation_accuracy, "Validation Loss:", validation_loss)

# Get predictions for the validation data
predictions = model.predict(validation_generator, verbose=1)

games = {
    0: 'AOE4',
    1: 'CS2',
    2: 'FIFA',
    3: 'FN',
    4: 'LOL',
    5: 'OW',
    6: 'RL',
    7: 'SC2',
    8: 'SSBM',
    9: 'VAL'
}

# Decode the predictions
predicted_labels = np.argmax(predictions, axis=1)

# Get the true labels
true_labels = validation_generator.classes

# Get the filenames
filenames = validation_generator.filenames

wrong_predictions = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
}

# Print predicted labels, true labels, and filenames
for i in range(len(predicted_labels)):
    if predicted_labels[i] != true_labels[i]:
        print(f"Filename: {filenames[i]}, Predicted: {games[predicted_labels[i]]}, True: {games[true_labels[i]]}")
        wrong_predictions[true_labels[i]] += 1


for i, wrong in wrong_predictions.items():
    print(f"Game: {games[i]}, Wrong: {wrong}")


# Test the model
# Set the path to your test image folder
test_image_folder = './images/test'

# Create an ImageDataGenerator for preprocessing test data
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

# Load the test data from the image folder
test_generator = test_datagen.flow_from_directory(
    test_image_folder,
    target_size=target,  # Adjust the target size if necessary
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False  # Important: Do not shuffle the data
)

# Make predictions on the test data
predictions = model.predict(test_generator)

# Get the predicted labels
predicted_labels = np.argmax(predictions, axis=1)

# Get the true labels
true_labels = test_generator.classes

# Evaluate the model
accuracy = np.mean(predicted_labels == true_labels)
print("Accuracy on test set:", accuracy)