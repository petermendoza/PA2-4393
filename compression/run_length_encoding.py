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
        counter = 1
        rle_code.append(binary_image[0, 0])
        for y in range(binary_image.shape[0]):
            for x in range(binary_image.shape[1]):
                # Check when current pixel is approaching end of image
                if y != binary_image.shape[0]-1 and x == binary_image.shape[1]-1:
                    if binary_image[y, x] == binary_image[y+1, 0]:
                        counter += 1
                    else:
                        rle_code.append(counter)
                        counter = 1
                # Final pixel
                elif y == binary_image.shape[0]-1 and x == binary_image.shape[1]-1:
                    rle_code.append(counter)
                else:
                    if binary_image[y, x] == binary_image[y, x+1]:
                        counter += 1
                    else:
                        rle_code.append(counter)
                        counter = 1

        return rle_code

    def decode_image(self, rle_code, height, width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        decoded_image = zeros((height, width), uint8)
        current_index = 1
        current_color = rle_code[0]
        for y in range(decoded_image.shape[0]):
            for x in range(decoded_image.shape[1]):
                if x == 0:
                    current_color = 0
                if rle_code[current_index] != 0:
                    decoded_image[y, x] = current_color
                    rle_code[current_index] -= 1
                else:
                    current_color = 255 - current_color
                    current_index += 1
                    decoded_image[y, x] = current_color
                    rle_code[current_index] -= 1
        return decoded_image
