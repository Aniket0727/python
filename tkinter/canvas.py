from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox


win=Tk()
win.title("Shop")
win.minsize(width=400,height=500)


can=Canvas(win)
cord=10,50,270,210
# can.create_arc(cord,start=0,extent=250,fill="red")
can.create_polygon(cord,fill="red")
can.place(x=300,y=500)
can.pack()


win.mainloop()