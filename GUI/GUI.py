from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

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



def executeImageProcessing():
    pf = drop.cget('text')
    if (pf == 'CMT'):
        print("Process CMT")
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


def chooseInputImage():
    filename = askopenfilename(filetypes=(("PNG files", "*.png")
                                                     , ("JPG files", "*.jpg;*.jpeg")
                                                     , ("All files", "*.*")))

    if (filename == ""):
        print("There's nothing here")
    else:
        im = ImageTk.PhotoImage(Image.open(filename))
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


root.title = "Team 5 Final Project"
root.mainloop()
