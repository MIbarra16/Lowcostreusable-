from tkinter import *
#from PIL import ImageTK,Image
root = Tk ()
root.title ('Low Cost Resuable Bioreactor UI')
def Turnoff():
    mylabel1 = Label(root, text="Bioreactor Turning Off")
    mylabel1.pack()

def Save():
    global n 
    global Runname_info1
    global Runname_info2
    global Runname_info3
    global Runname_info4
    global Runname_info5
    global Runname_info6

    for n in range(1,6):
        if n == 1 :
            pH_info1 = pH.get()
            Tempature_info1 = Tempature.get()
            Time_info1 = Time.get()
            DOpercent_info1 = DOpercent.get()
            Load_info1 = Load.get()
            Runname_info1 = Runname.get()
        elif n == 2: 
            pH_info2 = pH.get()
            Tempature_info2 = Tempature.get()
            Time_info2 = Time.get()
            DOpercent_info2 = DOpercent.get()
            Load_info2 = Load.get()
            Runname_info2 = Runname.get()
        elif n == 3: 
            pH_info3 = pH.get()
            Tempature_info3 = Tempature.get()
            Time_info3 = Time.get()
            DOpercent_info3 = DOpercent.get()
            Load_info3= Load.get()
            Runname_info3 = Runname.get()
        elif n == 4: 
            pH_info4 = pH.get()
            Tempature_info4 = Tempature.get()
            Time_info4 = Time.get()
            DOpercent_info4 = DOpercent.get()
            Load_info4 = Load.get()
            Runname_info4 = Runname.get()
        elif n == 5: 
            pH_info5 = pH.get()
            Tempature_info5 = Tempature.get()
            Time_info5 = Time.get()
            DOpercent_info5 = DOpercent.get()
            Load_info5 = Load.get()
            Runname_info5 = Runname.get()
        elif n==6: 
            pH_info6 = pH.get()
            Tempature_info6 = Tempature.get()
            Time_info6 = Time.get()
            DOpercent_info6 = DOpercent.get()
            Load_info6 = Load.get()
            Runname_info6 = Runname.get()
            print
 


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
    Run1button = Button(top1, textvariable = Runname_info1).pack()
    Run2button = Button(top1, textvariable = Runname_info2).pack()
    Run3button = Button(top1, textvariable = Runname_info3).pack()
    Run4button = Button(top1, textvariable = Runname_info4).pack()
    Run5button = Button(top1, textvariable = Runname_info5).pack()
    Run6button = Button(top1, textvariable = Runname_info6).pack()
    Backbutton2 = Button(top1, text = "Back", command = top1.destroy).pack()
def Customrun():
    top.withdraw
   
    global Tempature 
    global pH 
    global DOpercent 
    global Load 
    global Time 
    global Runname

    Tempature = IntVar()
    pH = IntVar()
    DOpercent = IntVar()
    Load = IntVar()
    Time = IntVar()
    top2 = Toplevel() 
    Runname = StringVar()

    top2.geometry("600x600")
    top2.title('Custom Run Window')

    Tempature_text = Label(text= "Input the Tempature:")
    Tempature_entry = Entry(top2, textvariable=Tempature)
    Tempature_entry.insert(0,"In Celsius")

    pH_text = Label(text="Input pH:")
    pH_entry= Entry(top2, textvariable=pH)
    pH_entry.insert(0,"Range 2.0-4.0")

    DOpercent_text = Label(text = "Input DO percentage:")
    DOpercent_entry= Entry(top2,textvariable=DOpercent)
    DOpercent_entry.insert(0,"Range 0 to 100%")

    Load_text = Label(text = "Input Biaxial Load:")
    Load_entry= Entry(top2,textvariable=Load)
    Load_entry.insert(0,"Range 8-10%")
   
    Time_text = Label(text = "Input Run Time:")
    Time_entry = Entry(top2,textvariable=Time)
    Time_entry.insert(0,"In minutes") 
    
    Runname_text = Label(text = "Input Run name Label:")
    Runname_entry = Entry(top2,textvariable=Runname)
    Runname_entry.insert = (0,"Input Run Label")
    
    Savebutton = Button(top2, text ="Submit", command = Save)

   
    Tempature_text.pack()
    Tempature_entry.pack()
    pH_text.pack()
    pH_entry.pack()
    DOpercent_text.pack()
    DOpercent_entry.pack()
    Load_text.pack()
    Load_entry.pack()
    Time_text.pack()
    Time_entry.pack()
    Runname_text.pack()
    Runname_entry.pack()
    Savebutton.pack()

    Backbutton3 = Button(top2, text = "Back", command = top2.destroy)
    Backbutton3.pack()

def new_func():
    global top2

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