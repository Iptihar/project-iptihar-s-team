import cv2
import numpy as np
from datetime import datetime

class PsuedocolorImageProcessing:

    def get_intensity_slicing(self, image):


        return image


    def get_intensity_color_transformation(self, image):

        
        return image

        
def main():
    
    input_image = cv2.imread("Lenna.png", 0)
    pip = PsuedocolorImageProcessing()

    #Write output file
    output_dir = 'PIP/output/'
        
    output_image_1 = pip.get_intensity_slicing(input_image)
    output_image_2 = pip.get_intensity_color_transformation(input_image)
        
    output_image_name = output_dir + "_Intensity_Slicing_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image_1)
    output_image_name = output_dir + "_Intensity_Color_Transformation_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, output_image_2)

if __name__ == "__main__":
    main()
