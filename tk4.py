import sys
from tkinter import *
from tkinter import filedialog


def mHello():
    mText=ment.get()
    mlabel1 = Label(myApp,text=mText).pack()

def myNew():
    mlabel1 = Label(myApp,text="YO").pack()

def myOpen():
    myOpen = filedialog.askopenfile()
    mlabel4 = Label(myApp,text=myOpen).pack()

def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        myApp.destroy()
        
    
myApp = Tk()
#create a string variable
ment = StringVar()

#set the size of window
myApp.geometry('450x450+200+200')

myApp.title('Myapp')

mLabel = Label(myApp,text='my label').pack()

mButton = Button(myApp,text ='OK', command = mHello).pack()

#set the ment variable from the text entry box
mEntry = Entry(myApp,textvariable=ment).pack()

#create the menubar
menubar = Menu(myApp)

#create the file component of that menubar
filemenu = Menu(menubar, tearoff=0)

#Add the sub headings to the file menu
filemenu.add_command(label="New", command=myNew)
filemenu.add_command(label="Open", command=myOpen)
filemenu.add_command(label="Save As...")
filemenu.add_command(label="Close", command=mQuit)

menubar.add_cascade(label="File",menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help docs")
helpmenu.add_command(label="About",command=mAbout)
menubar.add_cascade(label="Help",menu=helpmenu)



#add menubar to the window
myApp.config(menu=menubar)

myApp.mainloop()
