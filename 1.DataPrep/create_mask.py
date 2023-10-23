# Creates masks that removed non-road or vehicle assets
import os
import cv2
import numpy as np
print("import ok")

# Define list of object types to be masked, here sky and buildings
sky = np.array([255, 255, 255])
building = np.array([97, 97, 97])
print("defined objects to be masked")

# Create mask1:
mask_image = cv2.imread("../DATA/Source/Roadmarkings/171206_030550389_Camera_5_bin.png")
white = np.array([255, 255, 255])
mask1 = cv2.inRange(mask_image, white, white)
print("constant mask copied")

# loops through all files in folder
semantic_path = "../DATA/Source/Semantic/"

for im in os.listdir(semantic_path):
    # read im
    image_path = semantic_path + str(im)
    Label = cv2.imread(image_path)

    # select pixels with colours outlined by masked_objects
    mask_sky = cv2.inRange(Label, sky, sky)
    mask_building = cv2.inRange(Label, building, building)

    # add mask 1 as a mask
    combined_mask = mask1 + mask_building + mask_sky
    combined_mask = cv2.bitwise_not(combined_mask)

    # save mask in folder
    mask_path = "../DATA/Mask/" + str(im)
    cv2.imwrite(mask_path, combined_mask)
    print("generated mask " + str(im))

