import cv2
import numpy as np
from datetime import datetime

class ColorModelTransformation:

    def get_cyan(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  CYAN
            output: cyan color image """
        rows, cols, chans = image.shape

        red = image[:, :, 2]
        green = image[:, :, 1]
        blue = image[:, :, 0]

        output = np.ones((rows, cols, 4), np.uint8)
        for i in range(rows):
            for j in range(cols):
                r = 1 - red[i, j] / 255
                g = 1 - green[i, j] / 255
                b = 1 - blue[i, j] / 255
                k = min(r,g,b)

                output[i, j, 0] = (r - k) / (1 - k) * 300.
                output[i, j, 1] = (g - k) / (1 - k) * 300.
                output[i, j, 2] = 0
                output[i, j, 3] = k * 300.

        return output

    def get_magenta(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  MAGENTA
            output: magenta color image """
        rows, cols, chans = image.shape

        red = image[:, :, 2]
        green = image[:, :, 1]
        blue = image[:, :, 0]

        output = np.ones((rows, cols, 4), np.uint8)
        for i in range(rows):
            for j in range(cols):
                r = 1 - red[i, j] / 255
                g = 1 - green[i, j] / 255
                b = 1 - blue[i, j] / 255
                k = min(r, g, b)

                output[i, j, 0] = (r - k) / (1 - k) * 300.
                output[i, j, 1] = 0
                output[i, j, 2] = (b - k) / (1 - k) * 300.
                output[i, j, 3] = k * 300.

        return output

    def get_yellow(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  YELLOW
            output: yellow color image """
        rows, cols, chans = image.shape

        red = image[:, :, 2]
        green = image[:, :, 1]
        blue = image[:, :, 0]

        output = np.ones((rows, cols, 4), np.uint8)
        for i in range(rows):
            for j in range(cols):
                r = 1 - red[i, j] / 255
                g = 1 - green[i, j] / 255
                b = 1 - blue[i, j] / 255
                k = min(r, g, b)

                output[i, j, 0] = 0
                output[i, j, 1] = (g - k) / (1 - k) * 300.
                output[i, j, 2] = (b - k) / (1 - k) * 300.
                output[i, j, 3] = k * 300.

        return output

    def get_black(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  BLACK
            output: black color image """
        rows, cols, chans = image.shape

        red = image[:, :, 2]
        green = image[:, :, 1]
        blue = image[:, :, 0]

        output = np.ones((rows, cols, 4), np.uint8)
        for i in range(rows):
            for j in range(cols):
                r = 1 - red[i, j] / 255
                g = 1 - green[i, j] / 255
                b = 1 - blue[i, j] / 255
                k = min(r, g, b)

                output[i, j, 0] = 0
                output[i, j, 1] = (g - k) / (1 - k) * 300.
                output[i, j, 2] = (b - k) / (1 - k) * 300.
                output[i, j, 3] = k * 300.

        return output[:,:,3]

    def get_red(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  RED
            output: red color image """
        red = image[:, :, 2]

        output = np.zeros((red.shape[0], red.shape[1], 3),dtype=red.dtype)
        output[:, :, 2] = red
        return output

    def get_green(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  GREEN
            output: green color image """
        green = image[:, :, 1]

        output = np.zeros((green.shape[0], green.shape[1], 3), dtype=green.dtype)
        output[:, :, 1] = green
        return output

    def get_blue(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  BLUE
            output: blue color image """
        blue = image[:, :, 0]

        output = np.zeros((blue.shape[0], blue.shape[1], 3), dtype=blue.dtype)
        output[:, :, 0] = blue
        return output

    def get_hue(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  HUE
            output: hue image """
        hsi = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, i = cv2.split(hsi)
        return h

    def get_saturation(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  SATURATION
            output: saturation image """
        hsi = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, i = cv2.split(hsi)
        return s

    def get_intensity(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  INTENSITY
            output: intensity image """
        hsi = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, i = cv2.split(hsi)
        return i
        

def main():
    
    input_image = cv2.imread("Lenna.png")
    cmt = ColorModelTransformation()

    #Write output file
    output_dir = 'output/'
        
    output_image = cmt.get_black(input_image)

    cv2.imshow("Lenna", output_image)
    cv2.waitKey(0)

    output_image_name = output_dir + "_BLACK_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image)


if __name__ == "__main__":
    main()
