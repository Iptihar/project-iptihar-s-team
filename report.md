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









3. Smoothing and Sharpening: by Brad









4. Graphical User Interface: by Marcus