import cv2
import numpy as np
from datetime import datetime
import math

class PsuedocolorImageProcessing:
    def createGradient(self, grad):  # uses linear change
        ret = [0] * 256
        L = len(grad) - 1
        A = int(255 / (L))
        B = 255 / A

        current = grad[0]

        for i in range(0, 256):
            C = int((i - 1) / A)
            if (C >= L - 1):
                C = L - 1
            now = grad[C]
            then = grad[C + 1]

            if (now > then):
                current -= B
            elif (now < then):
                current += B

            ret[i] = math.floor(current + .5)

            if (ret[i] > 255):
                ret[i] = 255
            elif (ret[i] < 0):
                ret[i] = 0
        return ret  # returns an array

    def seperateColors(self, arr):
        r = []
        g = []
        b = []

        for i in range(len(arr)):
            r.append(arr[i][0])
            g.append(arr[i][1])
            b.append(arr[i][2])

        return (r, g, b)


    def pseudoColorImage(self, img, colors):
        (height, width) = img.shape  # height, width
        # ret = np.random.rand(height, width, 3)
        ret = np.zeros((height, width + 32, 3), np.uint8)
        (Rarr, Garr, Barr) = self.seperateColors(colors)
        Rarr2 = self.createGradient(Rarr)
        Garr2 = self.createGradient(Garr)
        Barr2 = self.createGradient(Barr)

        for i in range(height):
            for j in range(width + 32):
                ret[i][j] = (0, 0, 0)

                if (j >= width + 5):
                    intensity = 255 - int((i / height) * 255)
                    ret[i][j][2] = (Rarr2[intensity])  # R
                    ret[i][j][1] = (Garr2[intensity])  # G
                    ret[i][j][0] = (Barr2[intensity])  # B
                elif (j >= width and j < width + 5):
                    ret[i][j][2] = 255  # R
                    ret[i][j][1] = 255  # G
                    ret[i][j][0] = 255  # B

                if (j < width):
                    intensity = np.clip(img[i][j], 0, 255)
                    ret[i][j][2] = (Rarr2[intensity])  # R
                    ret[i][j][1] = (Garr2[intensity])  # G
                    ret[i][j][0] = (Barr2[intensity])  # B

        return ret

    def doSlice(self, img, lower, upper, dim, background):

        slicing = [0.0] * 256

        if (background):
            slicing[0] = 0.00390624
        else:
            slicing[0] = dim
        for i in range(1, 256):
            if (background):
                slicing[i] = 0.00390625 + slicing[i - 1]
            else:
                slicing[i] = dim
        for i in range(256):
            if (i >= lower and i <= upper):
                slicing[i] = 1

        img2 = img.copy()
        (height, width) = img.shape  # height, width
        for i in range(height):
            for j in range(width):
                img2[i][j] = img[i][j] * slicing[img[i][j]]
        return img2

        
def main():
    input_image = cv2.imread("camera4.jpg", 0)
    colors = ((0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 165, 0), (255, 0, 0), (255, 0, 255)) #note: this is reversed (low to high)
    pip = PsuedocolorImageProcessing()

    #Write output file
    output_dir = 'PIP/output/'
        


    lower = 150
    upper = 255
    dim = 0.1
    background = False
    output_image_1 = pip.doSlice(input_image, lower, upper, dim, background)
    '''
    lower = the lower end of the histogram to maintain
    upper = the higherend of the histogram to maintain
    anything out of that boundary is lowered by the dim.
    Background is a boolean that either keeps or discards the background
    
    '''
    output_image_2 = pip.pseudoColorImage(input_image, colors)
    '''
    colors is an array of 3 elements arrays (r,g,b), it is listed from low to high.
    In the above colors ranges from blue -> light blue -> green -> yellow -> red -> purple
    note: the image output will be slightly bigger than the input image because of the bar on the right side
    '''

    output_image_name = output_dir + "_Intensity_Slicing_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image_1)
    output_image_name = output_dir + "_Intensity_Color_Transformation_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, output_image_2)

if __name__ == "__main__":
    main()
