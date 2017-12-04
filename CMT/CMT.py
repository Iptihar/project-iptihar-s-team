import cv2
import numpy as np
from PIL import Image
from datetime import datetime

class ColorModelTransformation:

    def get_cyan(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  CYAN
            output: cyan color image """
        im = Image.fromarray(image.astype('uint8'), 'RGB')
        output = im.convert("CMYK")
        output1 = np.array(output)
        cyan = output1[:, :, 2]
        im = Image.new("CMYK", (cyan.shape[1], cyan.shape[0]), "white")
        output2 = np.array(im)
        output2[:, :, 2] = cyan

        return output2

    def get_magenta(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  MAGENTA
            output: magenta color image """
        im = Image.fromarray(image.astype('uint8'), 'RGB')
        output = im.convert("CMYK")
        output1 = np.array(output)
        magenta = output1[:, :, 1]
        im = Image.new("CMYK", (magenta.shape[1], magenta.shape[0]), "white")
        output2 = np.array(im)
        output2[:, :, 1] = magenta

        return output2

    def get_yellow(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  YELLOW
            output: yellow color image """
        im = Image.fromarray(image.astype('uint8'), 'RGB')
        output = im.convert("CMYK")
        output1 = np.array(output)
        yellow = output1[:, :, 0]
        im = Image.new("CMYK", (yellow.shape[1], yellow.shape[0]), "white")
        output2 = np.array(im)
        output2[:, :, 0] = yellow

        return output2

    def get_black(self, image):
        """input: rgb color image
            for GUI: need a round radio option button with label:  BLACK
            output: black color image """
        im = Image.fromarray(image.astype('uint8'), 'RGB')
        output = im.convert("CMYK")
        output = output.split()
        cmyk = []
        for i in range(4):
            cmyk.append(output[i].load())
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                black = min(cmyk[0][i,j], cmyk[1][i,j], cmyk[2][i,j])
                cmyk[3][i,j] = black

        k =  np.array(output[3])
        return k

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

    #change function below to test run
    output_image = cmt.get_intensity(input_image)

    cv2.imshow("Lenna", output_image)
    cv2.waitKey(0)

    output_image_name = output_dir + "_INTENSITY_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image)


if __name__ == "__main__":
    main()
