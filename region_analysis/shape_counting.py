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

        shapes = dict()
        region_number = 0
        pixel_count = 0
        smallest_x = 0
        biggest_x = 0
        smallest_y = 0
        biggest_y = 0
        shape = 'c'
        for key, value in region.items():
            pixel_count += 1
            region_number = key
            for item in value:
                if (smallest_x > item[1]):
                    smallest_x = item[1]
                if (biggest_x < item[1]):
                    biggest_x = item[1]
                if (smallest_y > item[0]):
                    smallest_y = item[0]
                if (biggest_y < item[0]):
                    biggest_y = item[0]
        if pixel_count > 10:
            if (biggest_x - smallest_x) == (biggest_y - smallest_y):
                shape = 'c'
                for key, value in region.items():
                    for item in value:
                        if (biggest_y, biggest_x) == item:
                            shape = 's'
            else:
                shape = 'e'
                for key, value in region.items():
                    for item in value:
                        if (biggest_y, biggest_x) == item:
                            shape = 'r'
            centroid = ((biggest_y+smallest_y)/2, (biggest_x+smallest_x)/2)
            shapes = {"Region": region_number,
                      "Centroid (in terms of (y,x))": centroid, "Area": pixel_count, "Shape": shape}
            print(shapes.items())
        return shapes

    def count_shapes(self, shapes_data):
        """Compute the count of shapes using the shapes data returned from identify shapes function
           takes as input
           shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
           returns: a dictionary with count of each shape
           Example return value: {'circles': 21, 'ellipses': 25, 'rectangles': 31, 'squares': 23}
           """
        return {"circles": 0, "ellipses": 0, "rectangles": 0, "squares": 0}

    def mark_image_regions(self, image, shapes_data):
        """Creates a new image with computed stats for each shape
        Make a copy of the image on which you can write text.
        takes as input
        image: binary image
        shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
        returns: image marked with center and shape_type"""

        return image
