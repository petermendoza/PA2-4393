class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                hist[image[x, y]] += 1

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
        threshold = len(hist)/2
        total_1 = 0
        total_2 = 0
        mean_1 = 0
        mean_2 = 0
        old_mean_1 = 0
        old_mean_2 = 0
        while abs(old_mean_1 - mean_1) > 1 and abs(old_mean_2 - mean_2) > 1:
            old_mean_1 = mean_1
            old_mean_2 = mean_2
            mean_1 = 0
            mean_2 = 0
            total_1 = 0
            total_2 = 0
            for x in hist:
                if x < threshold:
                    total_1 += hist[x]
                else:
                    total_2 += hist[x]
            for x in hist:
                if x < threshold:
                    mean_1 += (hist[x]/total_1) * x
                else:
                    mean_2 += (hist[x]/total_2) * x
            threshold = round((mean_1 + mean_2)/2)
        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the input image based on histogram analysis and thresholding
        takes as input
        image: a grey scale image
        threshold: to binarize the greyscale image
        returns: a binary image"""

        bin_img = image.copy()
        for y in bin_img.shape[0]:
            for x in bin_img.shape[1]:
                if bin_img[y, x] < threshold:
                    bin_img[y, x] = 0
                else:
                    bin_img[y, x] = 255
        return bin_img
