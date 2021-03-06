
import os
import glob
import time
from tkinter import*
import sys 
import gpiozero 

RELAY_PIN = 17#GPIO port 
relay = gpiozero.OutputDevice(RELAY_PIN, active_high = False, inital_value = False)

def RelayOO():
    relay.on()
    time.sleep(20)
    relay.off()


 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        Templabel.config(text = temp_c)
        return temp_c, temp_f

	
root = Tk()
root.title('Low Cost Resuable Bioreactor UI')
root.geometery('600x600')
Templabel = Label(root, text ="")
root.after(1000,read_temp)
RelayOO()

