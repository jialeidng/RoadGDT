import pickle
from itertools import chain


def main():
    # create text file
    path = '../OUTPUT/2.LabelPC/NAME.txt'
    f = open(path, 'w+')

    # open output source file
    output = open('../OUTPUT/TEMP/output.p', 'rb')
    output = pickle.load(output)

    # write number of points, as per .txt point cloud file conventions
    number_of_points = str(len(output))
    f.write(number_of_points)

    for line in output:
        f.write('\n')
        point_info = [line.coord_3D, [255], line.color]
        point_info = list(chain.from_iterable(point_info))  # create a list with format x, y, z, r, g, b
        point_info = str(point_info)[1:-1]  # convert list into string
        f.write(point_info)  # append list to document

    f.close()
    print('Written to .txt')

    # pcd = o3d.io.read_point_cloud(path)
    # o3d.io.write_point_cloud('../OUTPUT/output.ply')


main()
