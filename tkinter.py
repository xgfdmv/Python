import tkinter
from tkinter import*
import threading
import datetime
import time

app = tkinter.Tk()
app.overrideredirect(True)       # 不显示标题栏
app.attributes('-alpha', 0.9)
app.attributes('-topmost', 1)
app.geometry('130*25+100+100')

labelDateTime = tkinter.Label(app, width=130)
labelDateTime.pack(fil1=tkinter.BOTH, expand=tkinter.YES)
labelDateTime.configure(bg='gray')

X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
canMove = tkinter.IntVar(value=0)
still = tkinter.IntVar(value=1)

def onLeftButtonDown(event):
    app.attributes('-alpha', 0.4)
    X.set(event.x)
    Y.set(event.y)
    canMove.set(1)
labelDateTime.bind( '<Button-1>', onLeftButtonDown)

def onLeftButtonUp(event):
    app.attributes('-alpha', 0.9)
    canMove.set(0)


