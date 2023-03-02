class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256

        return hist

    def find_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold assuming that the input histogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value
        Note: Use the iterative method to calculate the histogram. Do not use the Otsu's method
        Write your code to compute the optimal threshold method.
        This should be implemented using the iterative algorithm discussed in class (See Week 4, Lecture 7, slide 42
        on teams). Do not implement the Otsu's thresholding method. No points are awarded for Otsu's method.
        """

        threshold = 0

        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the input image based on histogram analysis and thresholding
        takes as input
        image: a grey scale image
        threshold: to binarize the greyscale image
        returns: a binary image"""

        bin_img = image.copy()

        return bin_img


