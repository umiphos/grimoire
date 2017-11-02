#!/usr/bin/python
#coding=utf-8
from Tkinter import *
import tkFont

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def ledON():
	print("LED button pressed")
	
	if	(ledButton["text"]=="LED ON"):
		ledButton["text"] = "LED OFF"
	else:
		ledButton["text"] = "LED ON"
	
def exitProgram():
	print("Exit Button pressed")
	win.withdraw()
	mainwindowtoo()
	#win.quit()

def mainwindowtoo():
	win.title("First GUI")
	win.geometry('400x480')

	
	ledButton = Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 )
	ledButton.pack()
	
def mainwindow():
	win.title("First GUI")
	win.geometry('800x480')

	exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
	exitButton.pack(side = BOTTOM)

	ledButton = Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 )
	ledButton.pack()
mainwindow()
mainloop()
