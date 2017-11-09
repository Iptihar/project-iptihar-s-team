import cv2
import numpy as np
from datetime import datetime

class SmoothingAndSharpening:

    def get_smoothing(self, image):


        return image


    def get_sharpening(self, image):

        
        return image

        
def main():
    
    input_image = cv2.imread("Lenna.png", 0)
    sas = SmoothingAndSharpening()

    #Write output file
    output_dir = 'SAS/output/'
        
    output_image_1 = sas.get_smoothing(input_image)
    output_image_2 = sas.get_sharpening(input_image)
        
    output_image_name = output_dir + "_Smoothing_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image_1)
    output_image_name = output_dir + "_Sharpening_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, output_image_2)

if __name__ == "__main__":
    main()
