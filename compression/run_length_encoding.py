from dip import *


class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        rle_code = []
        current_color = binary_image[0, 0]
        value = 0
        for y in range(binary_image.shape[0]):
            for x in range(binary_image.shape[1]):
                if binary_image[y, x] == current_color:
                    value += 1
                else:
                    rle_code.append(value)
                    value = 0
                    current_color = binary_image[y, x]

        return rle_code  # replace zeros with rle_code

    def decode_image(self, rle_code, height, width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        decoded_image = zeros((height, width), uint8)
        current_index = 0
        current_color = 0
        list_tracker = rle_code
        for y in range(decoded_image.shape[0]):
            for x in range(decoded_image.shape[1]):
                if list_tracker[current_index] != 0:
                    decoded_image[y, x] = current_color
                    list_tracker[current_index] -= 1
                if list_tracker[current_index] == 0:
                    if current_color == 0:
                        current_color = 255
                    else:
                        current_color = 0
                    current_index += 1
                    decoded_image[y, x] = current_color
                    list_tracker[current_index] -= 1
        return decoded_image  # replace zeros with image reconstructed from rle_Code
