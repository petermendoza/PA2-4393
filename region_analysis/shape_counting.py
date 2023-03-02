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

        return regions

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

