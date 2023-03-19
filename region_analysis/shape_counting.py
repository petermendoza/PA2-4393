import dip
from dip import *


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
                    if image[y-1, x] == 255:
                        regions[(y, x)] = regions[(y-1, x)]
                    elif image[y, x-1] == 255:
                        regions[(y, x)] = regions[(y, x-1)]
                    else:
                        regions[(y, x)] = region_label
                        region_label += 1
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
        for x in region:
            if len(region[x]) > 10:
                shapes = dict()
                pixel_count = 0
                smallest_x = 0
                biggest_x = 0
                smallest_y = 0
                biggest_y = 0
                shape = 'c'
                for values in region[x]:
                    pixel_count += 1
                    if (smallest_x > values[1]):
                        smallest_x = values[1]
                    if (biggest_x < values[1]):
                        biggest_x = values[1]
                    if (smallest_y > values[0]):
                        smallest_y = values[0]
                    if (biggest_y < values[0]):
                        biggest_y = values[0]
                if (biggest_x - smallest_x) == (biggest_y - smallest_y):
                    shape = 'c'
                    for values in region[x]:
                        if (biggest_y, biggest_x) == values:
                            shape = 's'
                else:
                    shape = 'e'
                    for values in region[x]:
                        if (biggest_y, biggest_x) == values:
                            shape = 'r'
                centroid = ((biggest_y+smallest_y)/2, (biggest_x+smallest_x)/2)
                shapes = {"Region": x,
                          "Centroid (in terms of (y,x))": centroid, "Area": pixel_count, "Shape": shape}
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
                y_coord, x_coord), dip.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, dip.LINE_AA)
        return labeled_image
