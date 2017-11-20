from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from PIL import ImageDraw

funclist = ['CMT','PIP','SAS']

root = Tk()
root.minsize(1200,800)
root.maxsize(1200,800)
thelabel = Label(root,text="label")
thelabel.pack()
img = ImageTk.PhotoImage(Image.open("Lenna.png"))
preimagelabel = Label(root,image=img,width=500,height=500)
preimagelabel.size()
preimagelabel.place(x=50,y=50)
inputimage = img


def executeImageProcessing():
    pf = drop.cget('text')
    if (pf == 'CMT'):
        print("Process CMT")
        inimg = inputimage
        outimg = inimg#poimg = CMT.pseudoColorProcess(inimg,arg1,...)
        outimghist = getHistogram(outimg)
        poimg = ImageTk.PhotoImage(outimghist)
        postimagelabel.configure(image=poimg)
        postimagelabel.image = poimg
    elif (pf == 'PIP'):
        print("Process PIP")
    elif (pf == 'SAS'):
        print("Process SAS")

renderbutton = Button(root,text="Render",command=executeImageProcessing)
renderbutton.place(x=580,y=200)





postimagelabel = Label(root,image=img,width=500,height=500)
postimagelabel.size()
postimagelabel.place(x=650,y=50)

ProcessingFunction = funclist[0]

def updateArgumentsPanel():
    ProcessingFunction = drop.cget('text')


def choseSomething(event):
    updateArgumentsPanel()

def getHistogram(hinimage):
    can = Canvas()
    #can.postscript(file="histogram.ps",colormode="color")
    dims = (hinimage.width(),hinimage.height())
    print(dims[0])
    print(dims[1])
    histogramimage = Image.new(mode="RGB",size=dims,color=(255,255,255))

    draw = ImageDraw.Draw(histogramimage)
    #get the histogram data
    
    #draw the rectangles of a histogram
    draw.rectangle([0,0,hinimage.width()/2,hinimage.height()/2],fill="red")
    return histogramimage

def chooseInputImage():
    filename = askopenfilename(filetypes=(("PNG files", "*.png")
                                                     , ("JPG files", "*.jpg;*.jpeg")
                                                     , ("All files", "*.*")))

    if (filename == ""):
        print("There's nothing here")
    else:
        im = ImageTk.PhotoImage(Image.open(filename))
        inputimage = im

        preimagelabel.configure(image = im)
        preimagelabel.image = im


loadbutton = Button(root,text="Load Image",command=chooseInputImage)
#loadbutton.size(w=100,h=25)
loadbutton.place(x=50,y=580)
loadbutton.config(width = 10, height = 1)


var1 = StringVar()
var1.set(funclist[0])
drop = OptionMenu(root,var1,*funclist,command=choseSomething)
drop.pack()

updateArgumentsPanel()



#tabs
argumentnotebook = ttk.Notebook()
pippage = ttk.Frame(argumentnotebook)
cmtpage = ttk.Frame(argumentnotebook)
saspage = ttk.Frame(argumentnotebook)

w = Spinbox(pippage, from_=0, to=10)
w.pack()
argumentnotebook.add(pippage,text='PIP')
argumentnotebook.add(cmtpage,text='CMT')
argumentnotebook.add(saspage,text='SAS')
argumentnotebook.place(x=150,y=580)
argumentnotebook.configure(width=400,height=150)
#argumentnotebook.pack(expand=1, fill="both")





root.title = "Team 5 Final Project"
root.mainloop()
