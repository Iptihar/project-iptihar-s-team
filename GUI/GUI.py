from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image,ImageTk
from PIL import ImageDraw
import cv2


from PIP import PIP as PsuedocolorImageProcessing
from SAS import SAS as SmoothingAndSharpening
from CMT import CMT as ColorModelTransformation


funclist = ['CMT','PIP','SAS']

root = Tk()
root.minsize(1200,800)
root.maxsize(1200,800)


root.inputimagematrix = cv2.imread("Lenna.png",cv2.IMREAD_COLOR)
root.greyinputimagematrix = cv2.imread("Lenna.png",0)
img = ImageTk.PhotoImage(Image.open("Lenna.png"))
preimagelabel = Label(root,image=img,width=500,height=500)
preimagelabel.size()
preimagelabel.place(x=50,y=50)
inputimage = img

PIP = PsuedocolorImageProcessing.PsuedocolorImageProcessing()
CMT = ColorModelTransformation.ColorModelTransformation()
SAS = SmoothingAndSharpening.SmoothingAndSharpening();
def executeImageProcessing():
    pf = argumentnotebook.index("current")



    if (pf == 1):
        print("Process CMT")
        inimg = root.inputimagematrix

        # inimg.shape = (inputimage.width(),inputimage.height())

        c = CMTMode.get()

        outimg = None
        if (c == "R"):
            outimg = CMT.get_red(image=inimg)
        elif (c == "G"):
            outimg = CMT.get_green(image=inimg)
        elif (c == "B"):
            outimg = CMT.get_blue(image=inimg)
        elif (c == "C"):
            outimg = CMT.get_cyan(image=inimg)
        elif (c == "M"):
            outimg = CMT.get_magenta(image=inimg)
        elif (c == "Y"):
            outimg = CMT.get_yellow(image=inimg)
        elif (c == "K"):
            outimg = CMT.get_black(image=inimg)
        elif (c == "H"):
            outimg = CMT.get_hue(image=inimg)
        elif (c == "S"):
            outimg = CMT.get_saturation(image=inimg)
        else:
            outimg = CMT.get_intensity(image=inimg)


        cv2.imwrite("temp.png", outimg)


        poimg = ImageTk.PhotoImage(Image.open("temp.png"))  # ImageTk.PhotoImage(outimg)
        outimg = cv2.imread("temp.png", 0)
        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
        outputimage = outimg
    elif (pf == 0):
        print("Process PIP")
        inimg = root.greyinputimagematrix#inputimagematrix

        #inimg.shape = (inputimage.width(),inputimage.height())

        if (root.PIPPseudoOrSliceMode.get() == 0):
            outimg = PIP.pseudoColorImage(img=inimg,colors=PIPColorArray)
        else:
            outimg = PsuedocolorImageProcessing.intensitySlicing(self=root,img=inimg, colors=PIPColorArray)

        cv2.imwrite("temp.png", outimg)

        #outimghist = getHistogram(outimg)


        poimg = ImageTk.PhotoImage(Image.open("temp.png")) #ImageTk.PhotoImage(outimg)
        outimg = cv2.imread("temp.png",0)
        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
        outputimage = outimg
    elif (pf == 2):
        print("Process SAS")
        inimg = root.inputimagematrix  # inputimagematrix

        # inimg.shape = (inputimage.width(),inputimage.height())
        #'butterworth_low'
        outimg = inimg
        if (root.SASSmoothingOrSharpeningMode.get()=="Smoothing"):
            #Smoothing
            if (root.SASRGBHSVMode == 0):
                #rgb
                outimg = SAS.get_smoothing_RGB(image=inimg, filter="butterworth_low", cutoff=root.cutoffspinbox.get(), order=root.orderspinbox.get())#PIP.pseudoColorImage(img=inimg, colors=PIPColorArray)
            else:
                #hsi
                outimg = SAS.get_smoothing_HSI(image=inimg, filter="butterworth_low", cutoff=root.cutoffspinbox.get(),order=root.orderspinbox.get())  # PIP.pseudoColorImage(img=inimg, colors=PIPColorArray)
        else:
            #Sharpening
            if (root.SASRGBHSVMode == 0):
                #rgb
                outimg = SAS.get_sharpening_RGB(image=inimg, filter="butterworth_high", cutoff=root.cutoffspinbox.get(), order=root.orderspinbox.get())#PIP.pseudoColorImage(img=inimg, colors=PIPColorArray)
            else:
                #hsi
                outimg = SAS.get_sharpening_HSI(image=inimg, filter="butterworth_high", cutoff=root.cutoffspinbox.get(),order=root.orderspinbox.get())  # PIP.pseudoColorImage(img=inimg, colors=PIPColorArray)


        cv2.imwrite("temp.png", outimg)

        outimghist = getHistogram(outimg)

        poimg = ImageTk.PhotoImage(Image.open("temp.png"))  # ImageTk.PhotoImage(outimg)
        outimg = cv2.imread("temp.png", 0)
        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
        outputimage = outimg



renderbutton = Button(root,text="Render",command=executeImageProcessing)
renderbutton.place(x=580,y=200)





postimagelabel = Label(root,image=img,width=500,height=500)
postimagelabel.size()
postimagelabel.place(x=650,y=50)

ProcessingFunction = funclist[0]






def getHistogram(hinimage):
    can = Canvas()
    #can.postscript(file="histogram.ps",colormode="color")
    dims = hinimage.shape#(hinimage.width(),hinimage.height())
    print(dims)

    histogramimage = Image.new(mode="RGB",size=(dims[0],dims[1]),color=(255,255,255))
    #u = Image.new(histogramimage,size=(dims[0],dims[1]))

    draw = ImageDraw.Draw(histogramimage)
    #get the histogram data
    
    #draw the rectangles of a histogram
    draw.rectangle([0,0,dims[0]/2,dims[1]/2],fill="red")
    return histogramimage

ColorArray = []


def chooseInputImage():
    filename = askopenfilename(filetypes=(("PNG files", "*.png")
                                                     , ("JPG files", "*.jpg;*.jpeg")
                                                     , ("All files", "*.*")))

    if (filename == ""):
        print("There's nothing here")
    else:
        print(filename)
        #print(root.inputimagematrix)
        root.inputimagematrix =  cv2.imread(filename, cv2.IMREAD_COLOR)
        root.greyinputimagematrix = cv2.imread(filename, 0)
        print(root.greyinputimagematrix)
        im = ImageTk.PhotoImage(Image.open(filename))
        inputimage = im


        preimagelabel.configure(image = im)
        preimagelabel.image = im




loadbutton = Button(root,text="Load Image",command=chooseInputImage)
#loadbutton.size(w=100,h=25)
loadbutton.place(x=50,y=580)
loadbutton.config(width = 10, height = 1)








#tabs
argumentnotebook = ttk.Notebook()
pippage = ttk.Frame(argumentnotebook)
#Inputs:
#Color Array
PIPColorButtons = []
PIPColorArray = []

def onColorButtonPressed(index):
    print("The index is "+str(index))
    col = askcolor()
    if (col[0] != None):
        hex = col[1]
        col = col[0]

        col = (int(col[0]),int(col[1]),int(col[2]))
        PIPColorArray[index] = col
        PIPColorButtons[index].config(bg=hex)



def onAddButtonPressed(number):

    ind = len(PIPColorArray)
    col = askcolor()
    #print(col)
    if (col[0] != None):
        hex = col[1]
        col = col[0]

        col = (int(col[0]),int(col[1]),int(col[2]))



        localcolorbutton = Button(pippage, command=lambda: onColorButtonPressed(ind))
        localcolorbutton.config(width=2, height=1)
        localcolorbutton.place(x=290+(25*ind), y=0)
        colorsquarelabel = Label(pippage)
        colorsquarelabel.config(width=1, height=1)
        #colorsquarelabel.config(image=colorsquare)
        localcolorbutton.config(bg=hex)
        PIPColorArray.append(col)
        PIPColorButtons.append(localcolorbutton)

        if (len(PIPColorArray) > 0):
            removecolorbutton.config(state=NORMAL)
            clearcolorbutton.config(state=NORMAL)
        else:
            removecolorbutton.config(state=DISABLED)
            clearcolorbutton.config(state=DISABLED)
def onRemoveButtonPressed():

    if (len(PIPColorArray) > 0):
        PIPColorArray.remove(PIPColorArray[len(PIPColorArray)-1])
        b = PIPColorButtons[len(PIPColorButtons) - 1]
        b.destroy();
        PIPColorButtons.remove(PIPColorButtons[len(PIPColorButtons) - 1])
        if (len(PIPColorArray) > 0):
            removecolorbutton.config(state=NORMAL)
            clearcolorbutton.config(state=NORMAL)
        else:
            removecolorbutton.config(state=DISABLED)
            clearcolorbutton.config(state=DISABLED)

def onClearButtonPressed():
    while(len(PIPColorArray) > 0):
        PIPColorArray.remove(PIPColorArray[len(PIPColorArray)-1])
        b = PIPColorButtons[len(PIPColorButtons) - 1]
        b.destroy();
        PIPColorButtons.remove(PIPColorButtons[len(PIPColorButtons) - 1])
    if (len(PIPColorArray) > 0):
        removecolorbutton.config(state=NORMAL)
        clearcolorbutton.config(state=NORMAL)
    else:
        removecolorbutton.config(state=DISABLED)
        clearcolorbutton.config(state=DISABLED)


radiobuttonwidth = 10
radiobuttonheight = 1
radiojustification = RIGHT

colorarraylabel = Label(pippage,text="Color Array")
colorarraylabel.config(width = 10, height = 1)
colorarraylabel.place(x=0,y=0)

addcolorbutton = Button(pippage,text="Add",command=lambda: onAddButtonPressed(number=5))
addcolorbutton.config(width = 8, height = 1)
addcolorbutton.place(x=80,y=0)
removecolorbutton = Button(pippage,state=DISABLED,text="Remove",command=lambda: onRemoveButtonPressed())
removecolorbutton.config(width = 8, height = 1)
removecolorbutton.place(x=150,y=0)
clearcolorbutton = Button(pippage,state=DISABLED,text="Clear",command=lambda: onClearButtonPressed())
clearcolorbutton.config(width = 8, height = 1)
clearcolorbutton.place(x=220,y=0)

root.PIPPseudoOrSliceMode = IntVar()
root.PIPPseudoOrSliceMode.set(0)
pipPseudoRadiobutton = Radiobutton(pippage,text="Pseudo Image Coloring")
pipPseudoRadiobutton.config(width = int(radiobuttonwidth*1.75), height = radiobuttonheight,justif=LEFT,variable=root.PIPPseudoOrSliceMode,value=0)
pipPseudoRadiobutton.place(x=0,y=40)
pipIntensitySlicingRadiobutton = Radiobutton(pippage,text="Intensity Slicing")
pipIntensitySlicingRadiobutton.config(width = int(radiobuttonwidth*1.25), height = radiobuttonheight,justif=LEFT,variable=root.PIPPseudoOrSliceMode,value=1)
pipIntensitySlicingRadiobutton.place(x=0,y=80)



cmtpage = ttk.Frame(argumentnotebook)
#Inputs:
CMTPairs = [("R","R"),("G","G"),("B","B"),("C","C"),("M","M"),("Y","Y"),("K","K"),("H","H"),("S","S"),("I","I")]

CMTMode = StringVar()
CMTMode.set("R")

colorradiobutton_red = Radiobutton(cmtpage,text=CMTPairs[0][0])
colorradiobutton_red.config(width = radiobuttonwidth, height = radiobuttonheight,justif=radiojustification,variable=CMTMode,value=CMTPairs[0][1])
colorradiobutton_red.place(x=0,y=0)
colorradiobutton_green = Radiobutton(cmtpage,text=CMTPairs[1][0])
colorradiobutton_green.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[1][1])
colorradiobutton_green.place(x=0,y=50)
colorradiobutton_blue = Radiobutton(cmtpage,text=CMTPairs[2][0])
colorradiobutton_blue.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[2][1])
colorradiobutton_blue.place(x=0,y=100)

colorradiobutton_Cyan = Radiobutton(cmtpage,text=CMTPairs[3][0])
colorradiobutton_Cyan.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[3][1])
colorradiobutton_Cyan.place(x=100,y=0)
colorradiobutton_Magenta = Radiobutton(cmtpage,text=CMTPairs[4][0])
colorradiobutton_Magenta.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[4][1])
colorradiobutton_Magenta.place(x=100,y=33)
colorradiobutton_Yellow = Radiobutton(cmtpage,text=CMTPairs[5][0])
colorradiobutton_Yellow.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[5][1])
colorradiobutton_Yellow.place(x=100,y=66)
colorradiobutton_Key = Radiobutton(cmtpage,text=CMTPairs[6][0])
colorradiobutton_Key.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[6][1])
colorradiobutton_Key.place(x=100,y=100)

colorradiobutton_Hue = Radiobutton(cmtpage,text=CMTPairs[7][0])
colorradiobutton_Hue.config(width = radiobuttonwidth, height = radiobuttonheight,justif=radiojustification,variable=CMTMode,value=CMTPairs[7][1])
colorradiobutton_Hue.place(x=200,y=0)
colorradiobutton_Saturation = Radiobutton(cmtpage,text=CMTPairs[8][0])
colorradiobutton_Saturation.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[8][1])
colorradiobutton_Saturation.place(x=200,y=50)
colorradiobutton_Intensity = Radiobutton(cmtpage,text=CMTPairs[9][0])
colorradiobutton_Intensity.config(width = radiobuttonwidth, height = radiobuttonheight,justify=radiojustification,variable=CMTMode,value=CMTPairs[9][1])
colorradiobutton_Intensity.place(x=200,y=100)

saspage = ttk.Frame(argumentnotebook)
root.SASSmoothingOrSharpeningMode = StringVar(root)
root.SASSmoothingOrSharpeningMode.set("Smoothing") # initial value

SASModeMenu = OptionMenu(saspage, root.SASSmoothingOrSharpeningMode, "Smoothing", "Sharpening")
SASModeMenu.place(x=0,y=0)

#Inputs:
#Filter, Cutoff, Order
OrderVar = IntVar()
OrderVar.set(1)

root.orderspinbox = Spinbox(saspage, from_=1, to=10)
print(root.orderspinbox.get())
root.orderspinbox.config(width=4)
root.orderspinbox.place(x=50,y=40)
orderlabel = Label(saspage,text="Order")
orderlabel.config(width = 5, height = 1)
orderlabel.place(x=0,y=40)

root.cutoffspinbox = Spinbox(saspage, from_=1, to=10,increment=1)
print(root.cutoffspinbox.get())
root.cutoffspinbox.config(width=4)
root.cutoffspinbox.place(x=50,y=80)
cutofflabel = Label(saspage,text="Cutoff")
cutofflabel.config(width = 5, height = 1)
cutofflabel.place(x=0,y=80)

root.SASRGBHSVMode = IntVar()
root.SASRGBHSVMode.set(0)
sasRGBRadiobutton = Radiobutton(saspage,text="RGB")
sasRGBRadiobutton.config(width = int(radiobuttonwidth*.5), height = radiobuttonheight,justif=radiojustification,variable=root.SASRGBHSVMode,value=0)
sasRGBRadiobutton.place(x=0,y=110)
sasHSIRadiobutton = Radiobutton(saspage,text="HSI")
sasHSIRadiobutton.config(width = int(radiobuttonwidth*.5), height = radiobuttonheight,justif=radiojustification,variable=root.SASRGBHSVMode,value=1)
sasHSIRadiobutton.place(x=50,y=110)
#orderspinbox.config(width = 10, height = 1)


argumentnotebook.add(pippage,text='PIP')
argumentnotebook.add(cmtpage,text='CMT')
argumentnotebook.add(saspage,text='SAS')
argumentnotebook.place(x=150,y=580)
argumentnotebook.configure(width=600,height=150)
#argumentnotebook.pack(expand=1, fill="both")





root.title = "Team 5 Final Project"
root.mainloop()
