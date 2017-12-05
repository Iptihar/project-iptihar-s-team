                                 Color Image Processing
                                       by Team 5
                              (Iptihar, Julian, Brad, Marcus)

    The main objective of this project is to create a graphical user interface program that
capable of changing the color space of an image to another, add colors to a greyscale image
which cannot normally have it, and perform sharpening and smoothing algorithms over a color image.

    We have four members in our team and each of us is responsible for one component of the project.
Iptihar is responsible for color model transformation, Julian is responsible for pseudocolor image
processing, Brad is responsible for smoothing and sharpening, Marcus is responsible for graphical
user interface.

Prerequisites: please make sure your machine has Anaconda, downgraded python 3.5 as instruction in
blackboard, OpenCV, and latest version of pycharm IDE.

Running: in order to run the  GUI, open the project folder in pycharm, go to "Run" option on top
and select "Edit Configuration", then from the pop up window find "Script" and direct that path
to "C:\...\project folder\GUI\GUI.py", click "Apply" followed by "OK". Finally click the green run
button on top right side of IDE.

1. Color Model Transformation: by Iptihar

Input (for all functions): any RGB image with png or jpg format, make sure image was read before you
pass it to the function.
Output (for all functions): single image array with respect to different color channel (green, cyan,
hue...tec).
Testrun: you can test test run any single function seperately by changing line 132 in CMT.py file.
main function already included, can test run easily using IDE.
libraries used: cv2, numpy, PIL, datetime

    Color model transformation (CMY/CMT.py) involves splitting RGB image into three primary channels,
convert RGB image to CMYK mode and output four different channels (cyan, magenta, yellow, black), also
convert RGB image to HSI and output each one as a single output image.

    if you check out CMT.py file you will notice that i have written 10 separate functions to accomplish
this goal. Input for every function can be any RGB image with format of png or jpg, the output will be a
numpy image array with reagrds to different color channel. The main idea is to understand different color
modes that image possess and successfully split them. Functionality is successfully implemented in GUI,
user needs to select one color channel radio button and click "render",result image will be shown on right
side.

    There too many ways to split an RGB image into three primary colors, my method is first convert it to
numpy arrays, create a new blank image, take the desired channel of input image and paste it to the blank
image. The only difference in the process of RGB and CMYK is that we need to convert RGB mode image to
CMYK mode first, i used PIL library for that purpose. Then i created a blank CMYK mode image and paste
the desired channel to the blank image. I could have easily merge them and output as a whole CMYK image,
but the initial idea was to show main difference between them, and i think the best way to do it is to
output every single one as a different picture. Most of the functionality is accomplished by manually
defined functions, only some basic operations are done by built-in functions like read, write, show, image
and conver them to numpy array...etc.

2. Psuedocolor image Processing: by Julian
Input: A grayscale image and an array of colors (stored as an array of array, each array in the color array has 3 elements stored as an integer 0-255 as RGB)
Output: A psuedocolor color image, the output image is slightly larger because the gradient is added to the right side of the image. This does not happen for intensity slicing.

Both psuedocolor and intensity slicing work the same. The only difference is psuedocolor uses a blended gradient. 
Libraries used: cv2, math, numpy

---pseudoColorImage---
This function takes in the array of colors stored as [[R,G,B],[R,G,B], ... ]. It then separates the colors into 3 separate arrays. Each color is then blended in the rgb color space separately. Colors chosen from hsv value seem to not blend properly. Using prechosen colors in the gui seems to work properly. The function also adds a gradient to the right side of the image for comparison. The resulting image is a psuedocolor image based on the grayscale input image.

---intensitySlicing---
This function takes in the same inputs as the previous function. The difference between this function and the previous is this function does not blend the color gradient. Other than that, the function is the same.

---createGradient---
This function creates the gradient, it uses linear change. Each color channel is fed separately. Both input and output are arrays. The output is a 256 elements to create a gradient.

---seperateColors---
separated the colors array into 3 separate color arrays to feed into create gradient

Main function allows the module to be ran by itself.

The way the psuedocolor function works is it takes an array of colors. If intensity color is selected, the gradient is not blended, if not, the gradient is blended. Once that is determined. The gradient is created accordingly and applied. The gradient is set to take in the intensity value (from 0 - 255) and returns the color to apply to the pixel. Each pixel is then replaced with the corresponding value from the gradient. The resulting image is the psuedocolor image.


3. Smoothing and Sharpening: by Brad

Input(for all functions): any RGB image, a string filter("butterworth_high"/"butterworth_low"), and 2 integers cutoff, and order.

Outputs(get_smoothing_RGB / get_sharpening_RGB): An RGB image after applying smoothing or sharpening on it using the filter argument in the RGB colorspace.

Outputs(get_smoothing_HSI / get_sharpening_HSI): An RGB image after applying smoothing or sharpening on it using the filter argument in the HSI colorspace.

libraries used: cv2, numpy



get_smoothing_RGB / get_sharpening_RGB involves splitting an RGB image into 3 images (standard order of splitting in cv2 is blue, green, red).
then applying the smoothing or sharpening methods to each of the 3 images. In this implementation I applied the smoothing and sharpening methods in the images
frequency domains. After the necessary steps for frequency filtering is done for each image, blue, green, and red. I merged them back and displayed the resulting
RGB image.


get_smoothing_HSI / get_sharpening_HSI involves the same steps as before except you convert the RGB image into the HSI domain and apply
the frequency filtering only on the intensity image. Once finished I merged the intensity image back with the hue and saturation images.
Then converted that HSI image back into an RGB image for output.







4. Graphical User Interface: by Marcus

The Graphical User Interface was integrated into the project using the TKinter module that comes native to the
Python framework. We thought it was ideally basic to implement so that time would not be spent struggling to learn any
of the more advanced GUI frameworks or platforms that may be far more powerful than what TKinter has to offer.

Coming from IDE's that are equipped with GUI Design Editors for easily accessed visual design of user-created interfaces,
designing the GUI from code certainly felt like a trip to the dark-ages. While it was a mild inconvenience to write the
GUI in this way, the process is not an unfamiliar one. I understood the struggles having to manually integrate the GUI in
the source code itself as opposed to using an interface editor so it did not take as long for me to take care of the process
by tapping into my knowledge of past projects that demanded the writing of the GUI in this fashion.

Though my past experience faciliated the creation of the interface, TKinter had a handful of quirks that defied some of
the conventions that I had learned throughout previous projects. Such as the Width and Height of simple TKinter Widgets like
Buttons and Dropdowns. Before, I had thought that the quantities were in terms of the number of pixels across the parent container.
Instead, TKinter seems to measure X and Width in the length of the number of text characters (i.e. a width of 5 would stretch
the widget to match the length of a 5 letter word as if it were to appear on the screen); while it measures Height in terms of the
length of a number of lines of text laid out vertically. Its not hard to imagine entering a Y offset value of 30 which I initially
expected to move the widget downward 30 pixels, but to be completely confused by it's absence when in actuality, it is 30 lines down
and virtually located 12 inches off of the computer screen. Because of this unexpected convention, I ended up wasting a great deal
of time trying to figure out how the number system actually behaved as opposed to the more familiar convention of pixel quantities.

My Python experience was very minimal coming into this project, so this would naturally lead to even more pitfalls and road-blocks
to progress. The notion of variable scopes escaped me when doing work in Python, so I had assumed that all variables were global
unless they had an object preceding it that one intended to access. When one of TKinter's Button events were fired and called
a function I had designated for it to run when this occurs, the global variables I had attempted to reference would mysteriously
cease to exist, throwing errors in the program's output. This caused even more baffling disorientation and confusion, burning
even more precious time. Oddly enough, some variables were still available such as the Root container which holds all of the
other widgets in the GUI so I did what, to me, seemed like a novel, outside-of-the-box solution to my problem which is most likely
considered child's-play to seasoned Python professionals: instead of storing the variable in the 'global' scope, I placed the
the variables that I needed remote access for in the Root object. It was an effective tactic, but anyone who has even used Python
probably understands this concept; except me, apparently. Its just one more thing to add to the list of bumps that were encountered
while getting used to both TKinter and Python.

The integrated design of the 3 other Image Processing components created by my teammates was straight-forward and intuitive.
The execution of each function took a loadable Image on the left as an input, some additional arguments, and a press of
the Render button pushes the processed image into the output panel on the right side based on the context of the function tab.
They explained each of their tasks for me and designated what arguments they needed in order to effectively utilize the
component each of them were individually constructing. There were not any conflicts on how the arguments should be arranged
and I was in agreement with all of their requests. Color Model Transformation required me to learn to use Radio Buttons
and how to use them in a group with each Radio Button pointing to the desired Color Model. Smoothing and Sharpening required
the use of numeric variables with maximum and minimum limits so the logical widget for these arguments would be Spinboxes
that respect the appropriate range of values. Psuedo Image Processing required the use of an array of colors for input.
While there was a functionality for asking the user to choose a color, there was not an immediate widget for storing an array
of colors so I was responsible for creating that on my own.

The overall layout of the widgets and the context sensitive tab make for an intuitive and effective layout for easily executing
these useful Image Processing operations.