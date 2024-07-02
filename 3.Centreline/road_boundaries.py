from PIL import Image
from classes import get_pixel_info

def main():
    # Open image file, define line height and RGB of road surface
    image = Image.open('../OUTPUT/1.Dataprep/MERGED/171206_030550389_Camera_5_bin.png')
    y_coordinate = 1700
    road_surface = [49, 49, 49]

    line = get_line(image, y_coordinate)
    boundaries = find_boundaries(line)


def get_line(image, y_coordinate):
    # Get x,y coordinates of a line drawn across the image and their RGB values
    line = []
    width, height = image.size

    for x in range(width):  # Loop through each pixel in the horizontal line
        pixel = image.getpixel((x, y_coordinate))
        # pixel_info = get_pixel_info(x_coord=x, y_coord=y_coordinate, rgb=list(pixel))
        pixel_info = [x, y_coordinate, list(pixel)] # ask jasper why this does not work for datatype
        line.append(pixel_info)
    return line


def find_boundaries(line):
    # find boundaries between road surface and its neighbours - do not trigger at road markings
    boundaries =[] # list of final boundaries
    ignore = [] # list of RGB values to ignore

    for pixel in line:
        # if current pixel ==  pixel+1 :
            # go to next pixel
        # if current pixel != next pixel but is on the exclusion list:
            #
        # else:
            # append the pixel where the colour is the road surface



    return boundaries

main()