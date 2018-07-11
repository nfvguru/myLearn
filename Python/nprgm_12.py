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
    #handler.startFrame("LEFT", row=0, column=0)
    handler.startLabelFrame("Device Details", row=1, column=0)
    #handler.setBg("blue")
    #handler.setSticky("NEW")
    handler.setStretch("COLUMN")
    handler.addLabel("L1", "Device IP", 0, 0)
    handler.addEntry("DIP",0,1)
    handler.addButtons(["Connect"],ConnectDevice, 1,0,2)
    handler.addEmptyLabel("L2")
    #handler.setLabelBg("LEFT LABEL", "red")
    handler.stopLabelFrame()

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
    fh=open("devices.txt", "a")
    fh.write(IP + "," + PASS)
    fh.close

def addDevice():
    global handler
    print( "IP = " + handler.getEntry("DIP"))
    print( "PW = " + handler.getEntry("APW"))
    storeDevices(handler.getEntry("DIP"), handler.getEntry("APW"))
    handler.hideSubWindow("Device")

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
