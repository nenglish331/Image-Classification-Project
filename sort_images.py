import os
import shutil
import random

# Path to the image folder
root_folder = 'C:/Users/nengl/OneDrive/Classes/GVSU/!CIS 378 - Applied Machine Learning/Machine Learning Project'
images_dir = os.path.join(root_folder, 'images')

# Create the train folder
train_folder = os.path.join(images_dir, 'train')
# os.makedirs(train_folder, exist_ok=True)

val_folder = os.path.join(images_dir, 'validation')
# os.makedirs(val_folder, exist_ok=True)

test_folder = os.path.join(images_dir, 'test')
# os.makedirs(test_folder, exist_ok=True)

# Set the percentages for training, validation, and test
train_percentage = 0.6
val_percentage = 0.25
test_percentage = 0.15

# Iterate over the folders in the images folder
for folder_name in os.listdir(train_folder):
    game_dir = os.path.join(images_dir, folder_name)

    # valgamefolder = os.path.join(val_folder, folder_name)
    # if not os.path.exists(valgamefolder):
    #     os.makedirs(valgamefolder)

    # testgamefolder = os.path.join(test_folder, folder_name)
    # if not os.path.exists(testgamefolder):
    #     os.makedirs(testgamefolder)

    # train_dir = os.path.join(train_folder, folder_name)
    # os.makedirs(train_dir, exist_ok=True)
    # Create the train folder within each folder
    # val_dir = os.path.join(val_folder, folder_name)
    # os.makedirs(train_dir, exist_ok=True)
    # Create the train folder within each folder
    # test_dir = os.path.join(test_folder, folder_name)
    # os.makedirs(train_dir, exist_ok=True)

    # Move the subfolders to the group folder
    # for subfolder_name in os.listdir(game_dir):
    #     subfolder_path = os.path.join(game_dir, subfolder_name)
    #     if subfolder_name == 'train':
    #         for file in os.listdir(subfolder_path):
    #             shutil.move(os.path.join(subfolder_path, file), os.path.join(train_dir, file))
    #     elif subfolder_name == 'val':
    #         for file in os.listdir(subfolder_path):
    #             shutil.move(os.path.join(subfolder_path, file), os.path.join(val_folder, file))
    #     elif subfolder_name == 'test':
    #         for file in os.listdir(subfolder_path):
    #             shutil.move(os.path.join(subfolder_path, file), os.path.join(test_folder, file))


    # Make the folder if it doesn't already exist
    # if not os.path.exists(os.path.join(output_path, folder_name)):
    #     os.makedirs(os.path.join(output_path, folder_name))
    
    # Create the training, validation, and test folders within each folder
    # train_dir = os.path.join(game_dir, 'train')
    # val_dir = os.path.join(game_dir, 'val')
    # test_dir = os.path.join(game_dir, 'test')
    
    # os.makedirs(train_dir, exist_ok=True)
    # os.makedirs(val_dir, exist_ok=True)
    # os.makedirs(test_dir, exist_ok=True)
    
    # Get the list of hashed image files in the folder
    # image_files = os.listdir(game_dir)
    
    # Shuffle the image files randomly
    # random.shuffle(image_files)

    # num_images = 0
    # for group in os.listdir(game_dir):
    #     num_images += len(os.listdir(os.path.join(game_dir, group)))
    #     if group == 'train':
    #         num_train = len(os.listdir(train_dir))
    #     elif group == 'val':
    #         num_val = len(os.listdir(val_dir))
    #     elif group == 'test':
    #         num_test = len(os.listdir(test_dir))
    
    # Calculate the number of images for each split
    # num_train = int(num_images * train_percentage)
    # num_val = int(num_images * val_percentage)
    # num_test = num_images - num_train - num_val
    
    # Move the images to the respective folders
    # for i, image_file in enumerate(image_files):
    #     src_path = os.path.join(folder_path, image_file)
        
    #     if i < num_train:
    #         dst_path = os.path.join(train_dir, image_file)
    #     elif i < num_train + num_val:
    #         dst_path = os.path.join(val_dir, image_file)
    #     else:
    #         dst_path = os.path.join(test_dir, image_file)
        
    #     shutil.move(src_path, dst_path)
    
    # Check the percentage of images in each folder
    # train_percentage = num_train / num_images
    # val_percentage = num_val / num_images
    # test_percentage = num_test / num_images

    # print(f"Folder: {folder_name}")
    # print(f"Images: {num_images}")
    # print(f"Train Percentage: {train_percentage * 100:.3f}%")
    # print(f"Validation Percentage: {val_percentage * 100:.3f}%")
    # print(f"Test Percentage: {test_percentage * 100:.3f}%\n")
