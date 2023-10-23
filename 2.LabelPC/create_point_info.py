import pickle
from PIL import Image
from classes import ImageData, PointInfo


def main():
    # open all text as lines
    points3D = []
    images = []

    with open('../DATA/Pointcloud/points3D.txt') as lines:
        for line in lines.readlines():
            points3D.append(line)

    with open('../DATA/Pointcloud/images.txt') as lines:
        for line in lines.readlines():
            images.append(line)

    print(".txt files read")

    # populate 3D_points and images with info
    P_dict = import_3Dpoints(points3D)  # ImageData list and class to be filled in later
    Im_dict = import_images(images)

    # organise Im_dict into list in P_dict
    append_ImageData_list(P_dict, Im_dict)

    # write to temp file
    pickle.dump(P_dict, open('../DATA/Temp/P_dict.p', "wb"))
    print('Written temp pointinfo file')


def import_3Dpoints(points3D):
    # initiate list of points
    P_dict = []

    for line in points3D[3:]:  # select lines after preamble
        ID = int(line.split()[0])
        coord_str = line.split()[1:4]
        coord = []

        for i in coord_str:  # loop over each element in xyz
            i = float(i)  # turn to float
            coord.append(i)

        entry = PointInfo(point=ID, coord_3D=coord, asset_type=[], ImageData_list=[], color=[])  # input into dictionary
        P_dict.append(entry)

    print('IDs and coords entered')
    return P_dict


def import_images(images):
    Im_dict = []
    for line1, line2 in zip(images[4::2], images[5::2]):
        name = line1.split()[-1]
        seg_name = name.replace(".jpg", "_bin.png")
        line2 = line2.split(" ")
        l = len(line2)
        for i in range(0, l, 3):
            xyID = line2[i:i+3]
            xyID_int = int(xyID[2])
            if xyID_int != -1:
                x, y = round(float(xyID[0])), round(float(xyID[1]))
            else:
                continue
            RGB = get_RGB(seg_name, x, y)
            entry = ImageData(point=xyID_int, img_name=name, seg_name=seg_name, coord_2D=[x, y], RGB=RGB)
            Im_dict.append(entry)
        print("processed " + name)
    print("Image data imported")
    return Im_dict


def get_RGB(seg_name, x, y):
    path = "../DATA/MERGED/" + seg_name
    im = Image.open(path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    RGB = [r, g, b]
    return RGB


def append_ImageData_list(P_dict, Im_dict):
    for Im in Im_dict:
        for P in P_dict:
            if Im.point == P.point:
                P.ImageData_list.append(Im)
            else:
                continue

main()
