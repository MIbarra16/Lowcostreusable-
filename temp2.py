import tempfile
from tkinter import *
from xml.etree import ElementTree 
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
import threading 
from w1thermsensor import W1ThermSensor
import time
from tkinter import messagebox
import datetime 
import sys
import gpiozero
import glob
import csv 
import numpy as np
from datetime import datetime 

class settings:
    def __init__(self):
        self.name = "default"
        self.temperature = 0;
        self.do = 0;
        self.ph = 0;
        self.time = 0;
        self.biaxial = 0;
        self.tempread= 0;
        self.doread = 0;
        self.phread = 0;

sets = settings();

#from PIL import ImageTK,Image
root = Tk ()
root.title ('Low Cost Resuable Bioreactor UI')
def Turnoff():
    mylabel1 = Label(root, text="Bioreactor Turning Off")
    mylabel1.pack()

        

def Save():
    Temperature = Temperature_entry.get()
    pH = pH_entry.get()
    DOpercent = DOpercent_entry.get()
    Load = Load_entry.get()
    Time = Time_entry.get()
    Runname = Runname_entry.get()
    fileName = Runname + ".xml"
    #create xml 
    Runvalues = ET.Element('Run_Values')
    RunpH = ET.SubElement(Runvalues, 'Run_Inputted_pH')
    RunDO = ET.SubElement(Runvalues, 'Run_Inputted_DO')
    RunTemp = ET.SubElement(Runvalues,'Run_Inputted_Temperature')
    RunTime = ET.SubElement(Runvalues, 'Run_Inputted_Time')
    RunLoad = ET.SubElement(Runvalues, 'Run_Inputted_Load')
    RunLabel = ET.SubElement(Runvalues, 'Run_Inputted_Name')
    ET.dump(Runvalues)
    RunpH.text = pH
    RunDO.text = DOpercent
    RunTemp.text = Temperature
    RunTime.text = Time
    RunLoad.text = Load
    RunLabel.text = Runname
    
    tree = ET.ElementTree(Runvalues)
    tree.write(fileName, xml_declaration="xml")
    top2.destroy()
    
 #   with open (fileName, "wb") as files :
 #       tree.write(files)
 #   if __name__ == "__main__": 
 #       Save(Runname+".xml")

def Calibration():
    mylabel3 = Label(root, text="Calibration")
    mylabel3.pack()

def Helppage(): 
    mylabel3 = Label(root, text="Help page")
    mylabel3.pack() 
def Configuration():
    global top 
    #root.withdraw
    top = Toplevel()
    top.geometry("600x600")
    top.title('Configuration Window')
    Loadconfbutton = Button(top, text = "Load Run",command = Loadrun)
    Loadconfbutton.pack()
  
    Customizedconfbutton = Button(top, text = " Customize Run", command = Customrun)
    Customizedconfbutton.pack()
    
    Backbutton1 = Button(top, text = "Back", command = top.destroy)
    Backbutton1.pack()
def Loadrun():
    
    dbox = fd.askopenfile(mode='r', filetypes =[("XML Files", "*.xml" )])
    tree = ET.parse(dbox)
    root = tree.getroot()
    sets.temperature = root.find('Run_Inputted_Temperature').text
    sets.name = root.find('Run_Inputted_Name').text
    sets.do = root.find('Run_Inputted_DO').text
    sets.ph = root.find('Run_Inputted_pH').text
    sets.time = root.find('Run_Inputted_Time').text
    sets.biaxial = root.find('Run_Inputted_Load').text
    
    top3 = Toplevel()
    top3.geometry("600x600")
    top3.title('Load Run')
    RunNVar =Label(top3, text = "Run Name:"+sets.name)
    RunNVar.pack()
    RunTEVar =Label(top3, text = "Run Temperature:"+ str(sets.temperature))
    RunTEVar.pack()
    RunDVar =Label(top3, text = "Run Dissolved Oxygen Percentage:"+str(sets.do))
    RunDVar.pack()
    RunBVar =Label(top3, text = "Run Biaxial Load Percentage:"+str(sets.biaxial))
    RunBVar.pack()
    RunTIVar =Label(top3, text = "Run time: "+str(sets.time))
    RunTIVar.pack()
    RunPVar =Label(top3, text = "Run pH:"+str(sets.ph))
    RunPVar.pack()
    RunButton = Button(top3, text = "Run "+str(sets.name), command = RunIT)
    RunButton.pack()
    Backbutton4 = Button(top3, text = "Back", command = top3.destroy)
    Backbutton4
   
    #print(sets.name,sets.tempature,sets.do,sets.ph,sets.time,sets.biaxial)
   
    #set.tempature = root.find('Run_Inputted_Tempature')
    #tempature.value = root.find('Run_Inputted_Tempature').text
    #sets.name = root.find('Run_Inputted_Name').text
    #sets.name.value = root('Run_Inputted_Name').text
    #sets.do = root.find('Run_Inputted_DO').text
    #sets.ph = root.find('Run_Inputted_pH').text
    #sets.time = root.find('Run_Inputted_Time').text
    #set.biaxial = root.find('Run_Inputted_Load')
    #print(sets.name,sets.tempature,sets.do,sets.ph,sets.time,sets.biaxial)
    #file = open(dbox,'r')

    #print(dbox.read)

    #sets.tempature = dbox[0][1]
    #sets.name = dbox[0][1]
    #sets.do = dbox[][]
    #sets.ph = dbox[][]
    #sets.time = dbox[][]
    #sets.biaxial= dbox[][]

def Customrun():
    
    top.withdraw
   
    global Temperature 
    global pH 
    global DOpercent 
    global Load 
    global Time 
    global Runname
    global Temperature_entry 
    global pH_entry
    global DOpercent_entry 
    global Load_entry
    global Time_entry
    global Runname_entry
    global top2

    Temperature = IntVar()
    pH = IntVar()
    DOpercent = IntVar()
    Load = IntVar()
    Time = IntVar()
    top2 = Toplevel() 
    Runname = StringVar()
    Temperature_entry = IntVar()
    pH_entry = IntVar()
    DOpercent_entry = IntVar()
    Load_entry = IntVar()
    Time_entry = IntVar()
    Runname_entry = StringVar()


    top2.geometry("600x600")
    top2.title('Custom Run Window')

    Temperature_text = Label(top2,text= "Input the Temperature(Celsius):")
    Temperature_text.pack()
    Temperature_entry = Entry(top2, textvariable=Temperature)
    Temperature_entry.pack()
    #Tempature_entry.insert(0,"In Celsius")

    pH_text = Label(top2,text="Input pH(Range 6-8 pH):")
    pH_text.pack()
    pH_entry= Entry(top2, textvariable=pH)
    pH_entry.pack()
    #pH_entry.insert(0,"Range 2.0-4.0 ")

    DOpercent_text = Label(top2,text = "Input DO percentage(Range 0-100%):")
    DOpercent_text.pack()
    DOpercent_entry= Entry(top2,textvariable=DOpercent)
    DOpercent_entry.pack()
    #DOpercent_entry.insert(0,"Range 0 to 100%")

    Load_text = Label(top2, text = "Input Biaxial Load percentage(Range 8-10%):")
    Load_text.pack()
    Load_entry= Entry(top2,textvariable=Load)
    Load_entry.pack()
    #Load_entry.insert(0,"Range 8-10%")
   
    Time_text = Label(top2,text = "Input Run Time(minutes):")
    Time_text.pack()
    Time_entry = Entry(top2,textvariable=Time) 
    Time_entry.pack()
    #Time_entry.insert(0,"In minutes") 
    
    Runname_text = Label(top2,text = "Input Run Name Label:")
    Runname_text.pack()
    Runname_entry = Entry(top2,textvariable=Runname)
    Runname_entry.pack()
    #Runname_entry.insert = (0,"Run Name")
    
    Savebutton = Button(top2, text ="Submit", command = Save)
    Savebutton.pack()

  

    Backbutton3 = Button(top2, text = "Back", command = top2.destroy)
    Backbutton3.pack()
#def timerf():
#    if total_seconds > 0:
#        timerlabel.config(text = timer )
#        root.after(1000, timerf, total_seconds-1)
def TempC():
    sensor = W1ThermSensor()
    RawHigh = 99.6
    RawLow = 0.5 
    ReferenceHigh = 99.9
    ReferenceLow = 0 
    RawRange = RawHigh - RawLow 
    ReferenceRange = ReferenceHigh - ReferenceHigh
    RawValue = sensor.get_temperature()
    TempReading = (((RawValue-RawLow)*ReferenceRange)/RawRange)+ReferenceLow
    
    #TempRe.set=TempReading
    print("The temperature is %s celsius" % TempReading)
    TempR.config(text = float(TempReading))
    
    top4.after(1000,TempC)
    top4.update()

def TempD():
    global TempReading, TempR
    TempReading= StringVar()
    
    Templabel = Label(top4, text = "Tempature in Celsius")
    Templabel.place( x = 130 , y = 100)
    TempR = Label(top4, text = "0")
    TempR.place(x = 130, y =120)
    
    top4.after(1000, TempC)
    # TempRH.set("00")




    


   #os.system('modprobe w1-gpio')
   #os.system('modprobe w1-therm')
 
#    base_dir = '/sys/bus/w1/devices/'
#    device_folder = glob.glob(base_dir + '28*')[0]
#    device_file = device_folder + '/w1_slave'
#    Templabel = Label(top4, text = "Tempature in Celsius")
#    Templabel.pack() 
#    TempR = Label(top4, text = '' )
#    TempR.pack()
#    top4.after(1000,read_temp(device_file))
 

#def read_temp_raw(device_file):
#    f = open(device_file, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines
 
#def read_temp(device_file):
#    lines = read_temp_raw()
#    while lines[0].strip()[-3:] != 'YES':
#        time.sleep(0.2)
#        lines = read_temp_raw(device_file)
#    equals_pos = lines[1].find('t=')
#    if equals_pos != -1:
#        temp_string = lines[1][equals_pos+2:]
#        temp_c = float(temp_string) / 1000.0
#        temp_f = temp_c * 9.0 / 5.0 + 32.0
#        TempR.config(text = temp_c)
#        return temp_c, temp_f
    
def TimerD(): 
    global temp 
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
  
    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")
  
    # Use of Entry class to take input from the user
    TimeLabel = Label(top4, text = 'Run time Left:')
    TimeLabel.place(x = 100, y = 5)
    hourEntry= Entry(top4, width=3, font=("Arial",18,""),
                     textvariable=hour)
    hourEntry.place(x=80,y=20)
  
    minuteEntry= Entry(top4, width=3, font=("Arial",18,""),
                       textvariable=minute)
    minuteEntry.place(x=130,y=20)
  
    secondEntry= Entry(top4, width=3, font=("Arial",18,""),
                       textvariable=second)
    secondEntry.place(x=180,y=20)
    MinsI = int(sets.time)
    temp = int(MinsI)*60 
    
    while temp > -1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        top4.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            print("Run time for run is up")
            top4.withdraw
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
def HeatPad(timeleft, TemperatureReading):
    while timeleft > - 1: 
        if (TemperatureReading < int(set.temperature)):
            RELAY_PIN = 17  
            relay = gpiozero.OutputDevice(RELAY_PIN, active_high = False, inital_value = False)
            relay.on()
            print("Turn of relay")
            time.sleep(20)
            relay.off()
            print("Turn off relay")
def SaveCSV(TemperatureReading):
    dt = datetime.now()
    fn = str(dt) + ".csv"
    fn = fn.replace(":", "_")
    fn = fn.replace(" ", "_")
    fn = fn.replace("-", "_")
    x = [dt, TemperatureReading]
    with open(fn, 'w', newline='') as y:
        writer = csv.writer(y, dialect='excel')
        writer.writerows(x)
def RunIT(): 
    global top4
    top4 = Toplevel()
    top4.title(str(sets.name)+" Run")
    top4.geometry('600x600')

    t1 = threading.Thread(target = TimerD)
    t2 = threading.Thread(target = TempD, args = (temp, TempReading))
    t3 = threading.Thread(target = HeatPad, args =(TempReading))
    t1.start()
    t2.start()
    t3.start()
 #   t1.join()
 #   t2.join()
    #hour=StringVar()
    #minute=StringVar()
    #second=StringVar()
  
    ## setting the default value as 0
    #hour.set("00")
    #minute.set("00")
    #second.set("00")
  
    ## Use of Entry class to take input from the user
    #TimeLabel = Label(top4, text = 'Run time Left:')
    #TimeLabel.pack()
    #hourEntry= Entry(top4, width=3, font=("Arial",18,""),
    #                 textvariable=hour)
    #hourEntry.place(x=80,y=20)
  
    #minuteEntry= Entry(top4, width=3, font=("Arial",18,""),
    #                   textvariable=minute)
    #minuteEntry.place(x=130,y=20)
  
    #secondEntry= Entry(top4, width=3, font=("Arial",18,""),
    #                   textvariable=second)
    #secondEntry.place(x=180,y=20)
    #MinsI = int(sets.time)
    #temp = int(MinsI)*60 
    
    #while temp > -1:
         
    #    # divmod(firstvalue = temp//60, secondvalue = temp%60)
    #    mins,secs = divmod(temp,60)
  
    #    # Converting the input entered in mins or secs to hours,
    #    # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
    #    # 50min: 0sec)
    #    hours=0
    #    if mins >60:
             
    #        # divmod(firstvalue = temp//60, secondvalue
    #        # = temp%60)
    #        hours, mins = divmod(mins, 60)
         
    #    # using format () method to store the value up to
    #    # two decimal places
    #    hour.set("{0:2d}".format(hours))
    #    minute.set("{0:2d}".format(mins))
    #    second.set("{0:2d}".format(secs))
  
    #    # updating the GUI window after decrementing the
    #    # temp value every time
    #    top4.update()
    #    time.sleep(1)
  
    #    # when temp value = 0; then a messagebox pop's up
    #    # with a message:"Time's up"
    #    if (temp == 0):
    #        print("Run time for run is up")
    #        top4.withdraw
         
    #    # after every one sec the value of temp will be decremented
    #    # by one
    #    temp -= 1

     
    #

#creating a label widget 
root.title("Main Screen")
root.geometry("600x600")
Turnoffbutton1 = Button(root, text = "Turn Off", command =Turnoff)
Configurationbutton1= Button(root, text="Configuration", command = Configuration)
Calibrationbutton1 = Button(root, text = "Calibration")
Helppagebutton1= Button(root, text = "Help Page", command = Helppage)
#shoving on to the screen 
Turnoffbutton1.pack()
Configurationbutton1.pack()
Calibrationbutton1.pack()
Helppagebutton1.pack()


root.mainloop();
