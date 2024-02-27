from tkinter import ttk,filedialog
from tkinter import *
import os


win=Tk()
win.title("Tree View")
win.minsize(width=500,height=700)

scrollbarx=Scrollbar(win,orient=HORIZONTAL)
scrollbary=Scrollbar(win,orient=VERTICAL)

tree=ttk.Treeview(win,columns=("Name","Branch"),height=25,selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT,fill=Y)

scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=RIGHT,fill=X)

tree.heading('Name',text="Name",anchor=W)
tree.heading('Branch',text="Branch",anchor=W)

def file():
    global name
    name=filedialog.askopenfilename(parent=win,initialdir=os.getcwd())
    with open(name) as f:
        print(name)
        

btn=Button(text="select",command=file)
btn.place(x=150,y=500)
tree.pack()

win.mainloop()