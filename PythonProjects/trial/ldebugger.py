#!/usr/bin/python
import sys
import os
from appJar import gui


def ConnectDevice():
    global handler
    handler.clearLabel("L2")
    handler.setLabel("L2", "Connecting " + handler.getEntry("DIP"))

def processSelection(platform):
    global handler
    handler.startSubWindow(platform)
    handler.setSize(650,400)
    handler.setStretch("COLUMN")
    handler.startLabelFrame("Device Status ("+ platform +")", row=1 , column=0)
    handler.setStretch("COLUMN")
    handler.addLabel(platform+"watcher", "Watcher", 0, 0)
    handler.addNamedCheckBox("Enabled", platform+"watcherC", 0, 1)
    handler.addNamedButton("Disable", platform+"watcherB",None, 0, 2)
    handler.addLabel(platform+"altbtrace", "Alt_Backtrace", 1, 0)
    handler.addNamedCheckBox("Runnig", platform+"altC", 1, 1)
    handler.addNamedButton("Stop", platform+"altB",None, 1, 2)
    handler.addLabel(platform+"gdb", "GDB", 2, 0)
    handler.addNamedCheckBox("Not Installed",platform+"gdbC", 2, 1)
    handler.addNamedButton("Install",platform+"gdbB",None, 2, 2)
    handler.addLable
    handler.stopLabelFrame()
    handler.startLabelFrame("Debug ("+platform+")", row=2 , column=0)
    handler.addNamedButton("MP", platform+"mpB",None, 0, 0)
    handler.addNamedButton("SP", platform+"spB",None, 1, 0)
    handler.stopLabelFrame()
    handler.stopSubWindow()
    handler.showSubWindow(platform)

def getDeviceIP():
    global handler
    handler.showSubWindow("Device")
    #DIP = handler.textBox("", "Device IP", None)
    #print("Device IP " + DIP)

def menuPressFirst(who):
    #print("" + who)
    if who == "Exit" :
       sys.exit()
    if who == "New" :
       getDeviceIP();
       return
    processSelection(who)

def storeDevices(IP, PASS):
    global handler
    fh=open("devices.txt", "a")
    fh.write(IP + "," + PASS + "\n")
    fh.close
    handler.addMenuItem("Devices",IP,menuPressFirst)
    processSelection(IP)
   

def addDevice():
    global handler
    print( "IP = " + handler.getEntry("DIP"))
    print( "PW = " + handler.getEntry("APW"))
    storeDevices(handler.getEntry("DIP"), handler.getEntry("APW"))
    handler.hideSubWindow("Device")

def getStoredDevices():
    iplist=[]
    try:
        file = open("devices.txt", "r")
        for line in file:
           iplist.append(line.split(",")[0])
    except:
        iplist=[]        
    return iplist

def FirstColumnMenu(base):
   global handler 
   handler = base
   base.createMenu("Debug")
   base.addSubMenu("Debug", "Devices")
   base.addMenuSeparator("Debug")
   base.addMenuItem("Debug","Exit",menuPressFirst)
   formfactor = ["New"]
   base.addMenuList("Devices",formfactor,menuPressFirst)
   base.addMenuSeparator("Devices")
   ipList=getStoredDevices()
   base.addMenuList("Devices",ipList,menuPressFirst)
   base.startSubWindow("Device")
   base.setStretch("COLUMN")
   base.addLabel("L3","Device IP", 0,0)
   base.addEntry("DIP",0,1)
   base.addLabel("L4","Admin password", 1, 0)
   base.addSecretEntry("APW",1,1)
   base.addButtons(["Add"],addDevice, 2,0,2)
   base.stopSubWindow()
   base.hideSubWindow("Device")

def HandleMenu(base):
   #fileMenus = ["Open", "-", "Export", "Print", "-", "Close"]
   #base.addMenuList("File", fileMenus, menuPress)
   FirstColumnMenu(base)

def myGUIMain():
   app = gui("", "778x500")
   text=" -----     L A V A ' S    D E B U G G E R -------"
   #app.showSplash(text, fill='blue', stripe='black', fg='white', font=44)
   HandleMenu(app)
   app.go()


def main():
   myGUIMain()
   

#####################################33
sys.argv[1:]=[]
main()
