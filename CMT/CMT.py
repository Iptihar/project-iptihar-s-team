import cv2
import numpy as np
from datetime import datetime

class ColorModelTransformation:

    def get_rgb(self, image):


        return image


    def get_cmyk(self, image):

        
        return image

    def get_hsi(self, image):

        
        return image
        
        
def main():
    
    input_image = cv2.imread("Lenna.png", 0)
    cmt = ColorModelTransformation()

    #Write output file
    output_dir = 'CMT/output/'
        
    output_image_1 = cmt.get_rgb(input_image)
    output_image_2 = cmt.get_cmyk(input_image)
    output_image_3 = cmt.get_hsi(input_image)
        
    output_image_name = output_dir + "_RGB_" + datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, output_image_1)
    output_image_name = output_dir + "_CMYK_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, output_image_2)
    output_image_name = output_dir +  "_HSI_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, output_image_3)

if __name__ == "__main__":
    main()
