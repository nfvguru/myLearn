#!/usr/bin/python
import sys
if sys.version_info[0] <  3:
    from Tkinter import *
    from ttk import * 
else :
    from tkinter import *
    from tkinter.ttk import *

def simpleWindow():
    window = Tk()
    window.title("Welcome to first Tkinter app")
    window.mainloop()


# Text box, Button
def window1():
    window = Tk()
    window.title("Test Window 1")
    window.geometry('350x200')
    lbl = Label(window, text="Test1")
    lbl.grid(column=0, row=0)
    txt = Entry(window,width=10)
    txt.grid(column=1, row=0)
    txt.focus()
    def clicked():
       res = "Welcome to " + txt.get()
       lbl.configure(text= res)
       txt.configure(state="disabled")       
    btn = Button(window, text="Click", command=clicked)
    btn.grid(column=1, row=1)
    window.mainloop()

#Combo Box
def window2():
    window = Tk()
    window.title("Test 2")
    window.geometry('350x200')
    combo = Combobox(window)
    combo['values']= (1, 2, 3, 4, 5, "Text")
    combo.current(1) #set the selected item
    combo.grid(column=0, row=0)
    window.mainloop()

#Check Box
def window3():
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    chk_state = BooleanVar()
    chk_state.set(True) #set check state
    chk = Checkbutton(window, text='Choose', var=chk_state)
    chk.grid(column=0, row=0)
    window.mainloop()

#Radio Button
def window4():
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    selected = IntVar()
    rad1 = Radiobutton(window,text='First', value=1, variable=selected)
    rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
    rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
    def clicked():
        print(selected.get())
    btn = Button(window, text="Click Me", command=clicked)
    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)
    btn.grid(column=3, row=0)
    window.mainloop()

#Scrolled TExt Box
def window5():
    from tkinter import scrolledtext
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    txt = scrolledtext.ScrolledText(window,width=40,height=10)
    txt.grid(column=0,row=0)
    window.mainloop()


def main():
    #simpleWindow()
    #window1()
    #window2()
    #window3()
    #window4()
    #window5()
    print("Notihng");
    




main()
