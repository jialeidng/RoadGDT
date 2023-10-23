import pickle
from itertools import chain


def main():
    # create text file
    f = open('../OUTPUT/all.txt', 'w+')

    # open output source file
    output = open('../DATA/Temp/output.p', 'rb')
    output = pickle.load(output)

    # write number of points, as per .txt point cloud file conventions
    number_of_points = str(len(output))
    f.write(number_of_points)

    for line in output:
        f.write('\n')
        point_info = [line.coord_3D, line.color]
        point_info = list(chain.from_iterable(point_info))  # create a list with format x, y, z, r, g, b
        point_info = str(point_info)[1:-1]  # convert list into string
        f.write(point_info)  # append list to document

    f.close()
    print('Written to .txt')


main()
