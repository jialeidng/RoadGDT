import os
import cv2
import numpy as np
print("import ok")

def main():
    # Initiate path names
    SEMANTIC = "../DATA/Source/Semantic/"
    ROADMARKINGS = "../DATA/Source/Roadmarkings/"

    #initate path name lists
    semantic_paths = []
    marking_paths = []
    image_names = []

    for im in os.listdir(SEMANTIC):
        im = str(im)
        semantic_paths.append(SEMANTIC + im)
        marking_paths.append(ROADMARKINGS + im)
        image_names.append(im)

    print("created list of image paths for semantic and markings")

    for (i, j, k) in zip(semantic_paths, marking_paths, image_names):
        # open image and covert into RGB format
        semantic = cv2.imread(i)
        markings = cv2.imread(j)

        mask = create_mask(markings)
        MERGED = fuse(semantic, markings, mask)

        cv2.imwrite("../DATA/MERGED/" + k, MERGED)
        print("processed " + k)  # print image name being processed


def create_mask(markings_img):
    # select pixels with colours outlined by black
    black = np.array([0, 0, 0])
    markings_mask = cv2.inRange(markings_img, black, black) # Mask = 255 when black, 0 when roadmarkings
    return markings_mask

def fuse(semantic_img, markings_img, mask):

    # Zero background where we want to overlay
    semantic_img[mask == 0] = [0, 0, 0]
    # Add object to zeroed out space
    semantic_img = np.add(markings_img, semantic_img)
    return semantic_img


main()