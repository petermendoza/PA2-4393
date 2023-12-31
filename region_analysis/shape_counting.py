import dip
from dip import *
import math


class ShapeCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes as input:
        image: binary image
        return: a list/dict of regions
        """

        regions = dict()
        region_label = 0
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                if image[y, x] == 255:
                    if image[y, x-1] == 0 and image[y-1, x] == 0:
                        regions[(y, x)] = region_label
                        region_label = region_label + 1
                    if image[y, x-1] == 0 and image[y-1, x] == 255:
                        regions[(y, x)] = regions[(y-1, x)]
                    if image[y, x-1] == 255 and image[y-1, x] == 0:
                        regions[(y, x)] = regions[(y, x-1)]
                    if image[y, x-1] == 255 and image[y-1, x] == 255:
                        regions[(y, x)] = regions[(y-1, x)]
                        if regions[(y, x-1)] != regions[(y-1, x)]:
                            del regions[(y, x-1)]
                            regions[(y, x-1)] = regions[(y-1, x)]
        # Instead of making the dict key a coordinate, make the region number the key with the values being all coordinates
        sorted_regions = {}
        for key, value in regions.items():
            if value not in sorted_regions:
                sorted_regions[value] = []
            sorted_regions[value].append(key)
        return sorted_regions

    def identify_shapes(self, region):
        """Compute shape features area and centroid, and shape
        Ignore shapes smaller than 10 pixels in area.
        takes as input
        region: a list/dict of pixels in a region
        returns: shapes, a data structure with centroid, area, and shape (c, s, r, or e) for each region
        c - circle, s - squares, r - rectangle, and e - ellipse
        """

        # Please print your shape statistics to stdout, one line for each shape
        # Region: <region_no>, centroid: <centroid>, area: <shape area>, shape: <shape type>
        # Example: Region: 871, centroid: (969.11, 51.11), area: 707, shape: c

        final_dict = dict()
        for x in region.keys():
            # 40 instead of 10 to avoid extraneous regions
            if len(region[x]) > 40:
                shapes = dict()
                pixel_count = len(region[x])
                y_values = [p[0] for p in region[x]]
                x_values = [p[1] for p in region[x]]
                biggest_y = max(y_values)
                smallest_y = min(y_values)
                biggest_x = max(x_values)
                smallest_x = min(x_values)
                valid_region = True
                # Checking if length and width are around the same pixel length
                if abs((biggest_x - smallest_x) - (biggest_y - smallest_y)) < 3:
                    shape = 'c'
                    for values in region[x]:
                        if (biggest_y, biggest_x) == values or (biggest_y, smallest_x) == values or (smallest_y, biggest_x) == values or (smallest_y, smallest_x) == values:
                            shape = 's'
                else:
                    shape = 'e'
                    for values in region[x]:
                        if (biggest_y, biggest_x) == values or (biggest_y, smallest_x) == values or (smallest_y, biggest_x) == values or (smallest_y, smallest_x) == values:
                            shape = 'r'
                centroid = ((biggest_y+smallest_y)/2, (biggest_x+smallest_x)/2)
                shapes = {"Region": x,
                          "Centroid (in terms of (y,x))": centroid, "Area": pixel_count, "Shape": shape}
                # Removing regions with duplicate values
                for z in final_dict.keys():
                    dist_x = abs(centroid[1] - final_dict[z]
                                 ["Centroid (in terms of (y,x))"][1])
                    dist_y = abs(centroid[0] - final_dict[z]
                                 ["Centroid (in terms of (y,x))"][0])
                    if math.sqrt((dist_x**2)+(dist_y**2)) < 50:
                        if pixel_count < final_dict[z]["Area"]:
                            valid_region = False
                        else:
                            del final_dict[z]
                            break

                if valid_region == True:
                    print(shapes.items())
                    final_dict[x] = shapes

        return final_dict

    def count_shapes(self, shapes_data):
        """Compute the count of shapes using the shapes data returned from identify shapes function
           takes as input
           shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
           returns: a dictionary with count of each shape
           Example return value: {'circles': 21, 'ellipses': 25, 'rectangles': 31, 'squares': 23}
           """
        circles = 0
        ellipses = 0
        rectangles = 0
        squares = 0
        for x in shapes_data:
            if shapes_data[x]["Shape"] == 'c':
                circles += 1
            if shapes_data[x]["Shape"] == 'e':
                ellipses += 1
            if shapes_data[x]["Shape"] == 'r':
                rectangles += 1
            if shapes_data[x]["Shape"] == 's':
                squares += 1

        return {"circles": circles, "ellipses": ellipses, "rectangles": rectangles, "squares": squares}

    def mark_image_regions(self, image, shapes_data):
        """Creates a new image with computed stats for each shape
        Make a copy of the image on which you can write text.
        takes as input
        image: binary image
        shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
        returns: image marked with center and shape_type"""
        labeled_image = image
        for x in shapes_data:
            y_coord = round(shapes_data[x]["Centroid (in terms of (y,x))"][0])
            x_coord = round(shapes_data[x]["Centroid (in terms of (y,x))"][1])
            dip.putText(labeled_image, shapes_data[x]["Shape"], (
                int(x_coord), int(y_coord)), dip.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, dip.LINE_AA)
        return labeled_image
