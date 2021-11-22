from tkinter import *
#from PIL import ImageTK,Image
root = Tk ()
root.title ('Low Cost Resuable Bioreactor UI')
def Turnoff():
    mylabel1 = Label(root, text="Bioreactor Turning Off")
    mylabel1.pack()


def Calibration():
    mylabel3 = Label(root, text="Calibration")
    mylabel3.pack()

def Helppage(): 
    mylabel3 = Label(root, text="Help page")
    mylabel3.pack()
def Configuration():
    
    global top 
    top = Toplevel()
    top.geometry("600x600")
    top.title('Configuration Window')
    Loadconfbutton = Button(top, text = "Load Run",command = Loadrun).pack()
  
    Customizedconfbutton = Button(top, text = " Customize Run", command = Customrun ).pack()
    
    Backbutton1 = Button(top, text = "Back", command = top.destroy).pack()
def Loadrun():
    top.withdraw
    global top1 
    top1 = Toplevel()
    top1.geometry("600x600")
    top1.title('Load Run Window')
    Backbutton2 = Button(top1, text = "Back", command = top1.destroy).pack()
def Customrun():
    top.withdraw
    global top2
    global Tempature
    global pH 
    global DOpercent
    global Stretch 
    top2 = Toplevel() 
    top2.geometry("600x600")
    top2.title('Custom Run Window')
    Tempature = Entry(top2)
    Tempature.insert(0,"Input Tempatur")
    pH = Entry(top2)
    DOpercent  = Entry(top2)
    Stretch = Entry(top2)
    Tempature.pack()
    pH.pack()
    DOpercent.pack()
    Stretch.pack()

    Backbutton3 = Button(top2, text = "Back", command = top1.destroy).pack()

#creating a label widget 
mylabel = Label(root, text ="Main Screen")
root.geometry("600x600")
Turnoffbutton1 = Button(root, text = "Turn Off", command =Turnoff)
Configurationbutton1= Button(root, text="Configuration", command = Configuration)
Calibrationbutton1 = Button(root, text = "Calibration")
Helppagebutton1= Button(root, text = "Help Page", command = Helppage)
#shoving on to the screen 
mylabel.pack()
Turnoffbutton1.pack()
Configurationbutton1.pack()
Calibrationbutton1.pack()
Helppagebutton1.pack()


root.mainloop()