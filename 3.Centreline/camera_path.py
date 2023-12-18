# Get points and line of camera path
from classes import cam_inf
from pyquaternion import Quaternion
import numpy as np


def main():
    # open all text as lines
    images = []
    with open('../DATA/Pointcloud/images.txt') as lines:
        for line in lines.readlines():
            images.append(line)

    print(".txt file read")

    cam_inf_list = get_cam_inf(images)  # find camera position for each image
    cam_inf_list = convert_coords(cam_inf_list)

    write_trajectory(cam_inf_list)  # writen pure trajectory into file


def get_cam_inf(images):
    # go through every other line. Just get image name, and camera positions.
    # IMAGE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID, NAME
    cam_inf_list = []
    for image in images[4::2]:
        ID = image.split()[0]
        name = image.split()[-1]
        tra = list(map(float, image.split()[5:8]))
        rot = list(map(float, image.split()[1:5]))
        entry = cam_inf(image_ID=ID, image_name=name, translation=tra, rotation=rot, coords=[])
        cam_inf_list.append(entry)
        print("processed " + name)
    print("camera positions imported")
    return cam_inf_list


def convert_coords(cam_inf_list):
    # Convert quaternion to rotation matrix
    for i in cam_inf_list:
        rotation = Quaternion(np.array(i.rotation))
        rotation = np.linalg.inv(rotation.rotation_matrix)
        translation = np.array(i.translation)
        coords = np.dot(rotation, translation) * -1
        i.coords = coords
    return cam_inf_list


def write_trajectory(cam_inf_list):
    output = open('../OUTPUT/TEMP/trajectory_coords.txt', 'w+')
    output.write(str(len(cam_inf_list)))
    for line in cam_inf_list:
        output.write('\n')
        entry = str(line.coords)[1:-1]
        output.write(entry)
    output.close()
    print('Written path to .txt')


main()




