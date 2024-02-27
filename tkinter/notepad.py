from tkinter import *
from tkinter import ttk


win=Tk()
win.title("My Shop")
win.minsize(width=500,height=700)

i=filedialog.askopenfilename(initialdir=os.getcwd())

