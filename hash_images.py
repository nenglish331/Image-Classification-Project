import os
import hashlib

# Path to the image folder
root_folder = 'C:/Users/nengl/OneDrive/Classes/GVSU/!CIS 378 - Applied Machine Learning/Machine Learning Project'
image_folder = os.path.join(root_folder, 'images')
hashed_folder = os.path.join(root_folder, 'hashed_images')

# Loop through all files in the image folder
for folder in os.listdir(image_folder):
  game_folder = os.path.join(image_folder, folder)
  for filename in os.listdir(game_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
      # Generate a hash for the image file
      with open(os.path.join(game_folder, filename), 'rb') as file:
        image_data = file.read()
        hash_value = hashlib.md5(image_data).hexdigest()

      game_folder = os.path.join(image_folder, folder)
      hashed_game_folder = os.path.join(hashed_folder, folder)

      # Make the hashed game folder if it doesn't already exist
      if not os.path.exists(hashed_game_folder):
        os.makedirs(hashed_game_folder)

      # Rename the image file with the hash value
      new_filename = hash_value + os.path.splitext(filename)[1]
      os.rename(os.path.join(game_folder, filename), os.path.join(hashed_game_folder, new_filename))