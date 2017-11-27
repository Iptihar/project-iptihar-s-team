import cv2
import numpy as np
from datetime import datetime

from CMT import CMT as ColorModelTransformation

CMT = ColorModelTransformation.ColorModelTransformation()


class SmoothingAndSharpening:
    def get_smoothing_RGB(self, image, filter, cutoff, order):
        # Takes as input an RGB image outputs the smoothed RGB image based on filter, cutoff, order args in the RGB colorspace
        blue, green, red = cv2.split(image)

        if filter == 'butterworth_low':
            mask = np.zeros((image.shape[0], image.shape[1]), np.float64)
            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    d = np.sqrt((x - (image.shape[0] / 2)) ** 2 + (y - (image.shape[1] / 2)) ** 2)
                    mask[x, y] = 1 / (1 + (d / cutoff) ** (2 * order))
            fftred = np.fft.fft2(red)
            fftgreen = np.fft.fft2(green)
            fftblue = np.fft.fft2(blue)
            fftredshift = np.fft.fftshift(fftred)
            fftgreenshift = np.fft.fftshift(fftgreen)
            fftblueshift = np.fft.fftshift(fftblue)
            maskedimagered = np.zeros(red.shape, np.complex64)
            maskedimageblue = np.zeros(blue.shape, np.complex64)
            maskedimagegreen = np.zeros(green.shape, np.complex64)

            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    maskedimagered[x, y] = mask[x, y] * fftredshift[x, y]
                    maskedimageblue[x, y] = mask[x, y] * fftblueshift[x, y]
                    maskedimagegreen[x, y] = mask[x, y] * fftgreenshift[x, y]
            red_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimagered)))
            blue_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimageblue)))
            green_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimagegreen)))

            image = cv2.merge((blue_back, green_back, red_back))
        return image

    def get_smoothing_HSI(self, image, filter, cutoff, order):
        # Takes as input an RGB image outputs the smoothed RGB image based on filter, cutoff, order args in the HSI color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        intensity = hsv_image[:, :, 2]
        if filter == 'butterworth_low':
            mask = np.zeros((image.shape[0], image.shape[1]), np.float64)
            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    d = np.sqrt((x - (image.shape[0] / 2)) ** 2 + (y - (image.shape[1] / 2)) ** 2)
                    mask[x, y] = 1 / (1 + (d / cutoff) ** (2 * order))
            fftintensity = np.fft.fft2(intensity)
            fftintensityshift = np.fft.fftshift(fftintensity)
            maskedimageintensity = np.zeros(intensity.shape, np.complex64)

            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    maskedimageintensity[x, y] = mask[x, y] * fftintensityshift[x, y]
            intensity_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimageintensity)))

            hsv_image[:, :, 2] = intensity_back
            image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

        return image

    def get_sharpening_RGB(self, image, filter, cutoff, order):
        # Takes as input an RGB image outputs the sharpened RGB image based on filter, cutoff, order args
        blue, green, red = cv2.split(image)

        if filter == 'butterworth_high':
            mask = np.zeros((image.shape[0], image.shape[1]), np.float64)
            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    d = np.sqrt((x - (image.shape[0] / 2)) ** 2 + (y - (image.shape[1] / 2)) ** 2)
                    mask[x, y] = 1 - (1 / (1 + (d / cutoff) ** (2 * order)))

            fftred = np.fft.fft2(red)
            fftgreen = np.fft.fft2(green)
            fftblue = np.fft.fft2(blue)
            fftredshift = np.fft.fftshift(fftred)
            fftgreenshift = np.fft.fftshift(fftgreen)
            fftblueshift = np.fft.fftshift(fftblue)
            maskedimagered = np.zeros(red.shape, np.complex64)
            maskedimageblue = np.zeros(blue.shape, np.complex64)
            maskedimagegreen = np.zeros(green.shape, np.complex64)

            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    maskedimagered[x, y] = mask[x, y] * fftredshift[x, y]
                    maskedimageblue[x, y] = mask[x, y] * fftblueshift[x, y]
                    maskedimagegreen[x, y] = mask[x, y] * fftgreenshift[x, y]
            red_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimagered))) * 20
            blue_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimageblue))) * 20
            green_back = np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimagegreen))) * 20

            image = cv2.merge((blue_back, green_back, red_back))

        return image

    def get_sharpening_HSI(self, image, filter, cutoff, order):
        # Takes as input an HSI image outputs the sharpened HSI image based on filter, cutoff, order args
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        intensity = hsv_image[:, :, 2]
        if filter == 'butterworth_high':
            mask = np.zeros((image.shape[0], image.shape[1]), np.float64)
            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    d = np.sqrt((x - (image.shape[0] / 2)) ** 2 + (y - (image.shape[1] / 2)) ** 2)
                    mask[x, y] = 1 / (1 + (d / cutoff) ** (2 * order))
                    mask[x, y] = 1 - mask[x, y]
            fftintensity = np.fft.fft2(intensity)
            fftintensityshift = np.fft.fftshift(fftintensity)
            maskedimageintensity = np.zeros(intensity.shape, np.complex64)

            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    maskedimageintensity[x, y] = mask[x, y] * fftintensityshift[x, y]
            intensity_back = 20 * np.abs(np.fft.ifft2(np.fft.ifftshift(maskedimageintensity)))

            hsv_image[:, :, 2] = intensity_back
            image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        return image


def main():
    input_image = cv2.imread("Lenna.png")
    sas = SmoothingAndSharpening()

    # Write output file
    output_dir = 'output/'
    filter = 'butterworth_high'
    cutoff = min(input_image.shape[0], input_image.shape[1]) / 2
    order = 2
    output_image_1 = sas.get_smoothing_RGB(input_image, filter, cutoff, order)
    output_image_2 = sas.get_sharpening_RGB(input_image, filter, cutoff, order)

    output_image_name = output_dir + "_Smoothing_" + datetime.now().strftime("%m%d-%H%M%S") + ".png"
    cv2.imwrite(output_image_name, output_image_1)
    output_image_name = output_dir + "_Sharpening_" + datetime.now().strftime("%m%d-%H%M%S") + ".png"
    cv2.imwrite(output_image_name, output_image_2)


if __name__ == "__main__":
    main()
