import os

def delete_every_other_image(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over the files and delete every other image
    for index, file_name in enumerate(file_list):
        if index % 2 == 1:  # Skip every other image
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_name}")

# Specify the path to the folder containing the images
folder_path = "../DATA/Source/Colourimage"

# Call the function to delete every other image
delete_every_other_image(folder_path)
