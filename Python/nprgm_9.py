#!/usr/bin/python
import sys
import os


def myGUITest():
   from appJar import gui
   app = gui()
   app.addLabel("title", "My First GUI with appJar")
   app.setLabelBg("title","red")
   app.go()

def loginGUI():
   # import the library
   from appJar import gui

   # handle button events
   def press(button):
      if button == "Cancel":
          app.stop()
      else:
          usr = app.getEntry("Username")
          pwd = app.getEntry("Password")
          print("User:", usr, "Pass:", pwd)

   # create a GUI variable called app
   app = gui("Login Window", "378x265")
   app.setBg("orange")
   app.setFont(18)

   # add & configure widgets - widgets get a name, to help referencing them later
   app.addLabel("title", "Welcome to appJar")
   app.setLabelBg("title", "blue")
   app.setLabelFg("title", "orange")

   app.addLabelEntry("Username")
   app.addLabelSecretEntry("Password")

   # link the buttons to the function called press
   app.addButtons(["Submit", "Cancel"], press)

   app.setFocus("Username")

   # start the GUI
   app.go()


def main():
    if os.path.isdir("./appJars") == False:
        print("\n 1. Download and Install appJar from {} to load GUI".format("http://appjar.info"))
        print(" =>     How to Install: Just unzip appJar to the Python Directory");
        print("\n 2. Also should install relvant tkinter for the python version in use")
        print(" =>     For Eg. sudo  apt-get install python2.7-tk\n")
        return   
    myGUITest()
    loginGUI()

main()
