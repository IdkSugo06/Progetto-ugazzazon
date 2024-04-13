import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from threading import *
import time

root = tk.Tk()
root.geometry("800x800")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.grid_propagate(False)

canvasPrincipale = tk.Canvas(master = root)
canvasPrincipale.grid(row = 0, column=0, sticky= "nsew")
canvasPrincipale.columnconfigure(0, weight=1)
canvasPrincipale.columnconfigure(1, weight=1)
canvasPrincipale.grid_propagate(False)

littleFrame = tk.Frame(master = canvasPrincipale, background= "red")
littleFrame.place(x = 100, y = 100, height=300, width=300)
littleFrame.rowconfigure(0,weight=1)
littleFrame.rowconfigure(1,weight=1)
littleFrame.columnconfigure(0,weight=1)
littleFrame.grid_propagate(False)

framesuperiore = tk.Frame(master = littleFrame, background= "red")
framesuperiore.grid(row = 0, column= 0, sticky="nsew")
framesuperiore.rowconfigure(0,weight=1)
framesuperiore.columnconfigure(0,weight=1)
framesuperiore.grid_propagate(False)

canvas = None
w = 0
h = 0
img = Image.open("IMG_DEFANTEPRIMA copy.jpeg")
imgTK = ImageTk.PhotoImage(img)
def canvasResize(event):
    global w,h, img, imgTK
    print("configure called" ,w,h)
    w = event.width
    h = event.height
    canvas.create_image(w/2, h/2, image = imgTK, anchor = "center")

canvas = tk.Canvas(master = framesuperiore, background="pink", scrollregion=(0,0,2000,5000))
canvas.grid(row = 0, column= 0, sticky="nsew")
canvas.bind("<Configure>", canvasResize)
canvas.bind("<MouseWheel>", lambda event : canvas.yview_scroll(-int(event.delta/60), "units"))
print(type(canvasResize))
h = canvas.winfo_reqwidth()
w = canvas.winfo_reqheight()
print(w,h)

def funct():
    i = 0
    time.sleep(3)
    while i < 10000:
        littleFrame.place(x = 100, y = 100, height=100 + i, width=100 + i)
        i+=1
        time.sleep(1)

def funct2(**args):
    print("a")
    return

funct2()

t = Thread(target=funct)
#t.start()
root.mainloop()
t.join()