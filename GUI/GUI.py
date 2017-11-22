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


inputimagematrix = cv2.imread("Lenna.png",0)
img = ImageTk.PhotoImage(Image.open("Lenna.png"))
preimagelabel = Label(root,image=img,width=500,height=500)
preimagelabel.size()
preimagelabel.place(x=50,y=50)
inputimage = img

PIP = PsuedocolorImageProcessing.PsuedocolorImageProcessing()

def executeImageProcessing():
    pf = argumentnotebook.index("current")



    if (pf == 1):
        print("Process CMT")
        inimg = inputimage

        outimg = inimg#poimg = CMT.pseudoColorProcess(inimg,arg1,...)
        outimghist = getHistogram(outimg)
        poimg = ImageTk.PhotoImage(outimghist)


        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
    elif (pf == 0):
        print("Process PIP")
        inimg = inputimagematrix

        #inimg.shape = (inputimage.width(),inputimage.height())

        outimg = PIP.pseudoColorImage(img=inimg,colors=PIPColorArray)
        cv2.imwrite("temp.png", outimg)

        outimghist = getHistogram(outimg)


        poimg = ImageTk.PhotoImage(Image.open("temp.png")) #ImageTk.PhotoImage(outimg)
        outimg = cv2.imread("temp.png",0)
        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
        outputimage = outimg
    elif (pf == 2):
        print("Process SAS")

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

        inputimagematrix = cv2.imread("Lenna.png", 0)
        im = ImageTk.PhotoImage(Image.open(filename))
        inputimage = im


        preimagelabel.configure(image = im)
        preimagelabel.image = im
        loadbutton.destroy()



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
    #col = askcolor()
    #if (col[0] != None):
        #replace the old button



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
        localcolorbutton.place(x=220+(25*ind), y=0)
        colorsquarelabel = Label(pippage)
        colorsquarelabel.config(width=1, height=1)
        #colorsquarelabel.config(image=colorsquare)
        localcolorbutton.config(bg=hex)
        PIPColorArray.append(col)
        PIPColorButtons.append(localcolorbutton)



    removecolorbutton.config(state=NORMAL)
def onRemoveButtonPressed():

    if (len(PIPColorArray) > 0):
        PIPColorArray.remove(len(PIPColorArray)-1)
        PIPColorButtons.remove(len(PIPColorButtons) - 1)
        if (len(PIPColorArray) > 0):
            removecolorbutton.config(state=NORMAL)
        else:
            removecolorbutton.config(state=DISABLED)


colorarraylabel = Label(pippage,text="Color Array")
colorarraylabel.config(width = 10, height = 1)
colorarraylabel.place(x=0,y=0)

addcolorbutton = Button(pippage,text="Add",command=lambda: onAddButtonPressed(number=5))
addcolorbutton.config(width = 8, height = 1)
addcolorbutton.place(x=80,y=0)
removecolorbutton = Button(pippage,state=DISABLED,text="Remove",command=lambda: onRemoveButtonPressed())
removecolorbutton.config(width = 8, height = 1)
removecolorbutton.place(x=150,y=0)


cmtpage = ttk.Frame(argumentnotebook)
#Inputs:

saspage = ttk.Frame(argumentnotebook)
#Inputs:

#w = Spinbox(pippage, from_=0, to=10)
#w.pack()

argumentnotebook.add(pippage,text='PIP')
argumentnotebook.add(cmtpage,text='CMT')
argumentnotebook.add(saspage,text='SAS')
argumentnotebook.place(x=150,y=580)
argumentnotebook.configure(width=600,height=150)
#argumentnotebook.pack(expand=1, fill="both")





root.title = "Team 5 Final Project"
root.mainloop()
