# tkinter 31/08/2023

from tkinter import *
from tkinter import ttk,filedialog
from tkinter import messagebox
from tkinter import *
import os


    
win=Tk()
win.title("My Shop")
win.minsize(width=500,height=700)
# win.minsize(width=200,height=300)

def fun():
    if var.get()=="":
        messagebox.showwarning("Warning","Please Enter Deatils")
        a=var.get()
        l2.config(text=a)
    else:
        # messagebox.showinfo("Your Data",var.get())
        messagebox.askyesno("IMP","Do you want exit")
        win.destroy()


# Label
l=Label(text="My Label",bg="black",fg="white", width="7",height="1")
# l.pack()
# l.grid(row=4,column=6)
l.place(x=100,y=50)


l2=Label(text="My Value",bg="black",fg="white", width="7",height="1")
l2.place(x=160,y=160)

# Input field
var=StringVar()
e=Entry(bd='5',fg='red',font='arial',width='20', textvariable=var)
e.place(x=160,y=50)

e=ttk.Entry(width=20)
e.place(x=250,y=90)


# Button 
b=Button(bg='green',fg='white',width='10',text='Submit',bd=4, command=fun)
b.place(x=140,y=100)

# Combobox
cb=ttk.Combobox(width=10)
cb['state']="readonly"
cb['values']=("Aniket","Omkar","Rahul","Yash","Yash")
# cb.current(3)
cb.place(x=130,y=200)

# CheckButton

def fun3():
    print(a1.get())
    print(a2.get())
    print(a3.get())
    # print("hiiiiiii")

a1=IntVar()
a2=IntVar()
a3=IntVar()


cb1=Checkbutton(text="Male",variable=a1,onvalue=1,offvalue=0)
cb1.place(x=100,y=230)

cb2=Checkbutton(text="Female",variable=a2,onvalue=1,offvalue=0)
cb2.place(x=100,y=250)

cb3=Checkbutton(text="Other",variable=a3,onvalue=1,offvalue=0)
cb3.place(x=100,y=270)


btn=Button(text="Submit",command=fun3)
btn.place(x=120,y=300)

# Radio Button

def fun2():
    if(var2.get()==2):
        print("Female")
    elif(var2.get()==1):
        print("Male")
    else:
        print("Other")
    
var2=IntVar()

rb=Radiobutton(win,text="Male",value=1,variable=var2)
rb.place(x=100,y=350)

rb2=Radiobutton(win,text="Female",value=2,variable=var2)
rb2.place(x=100,y=370)

rb2=Radiobutton(win,text="Other",value=3,variable=var2)
rb2.place(x=100,y=390)

btn=Button(text="Submit",command=fun2)
btn.place(x=130,y=420)


# List

def delt():
    list.delete(ANCHOR)
    
list=Listbox()
list.place(x=200,y=250)
items=["Aniket","Omkar","Rahul","Yash","Ashutosh"]
for i in items:
    list.insert(END,i)

bt=Button(text="Delete",command=delt)
bt.place(x=240,y=430)


# Canvas

# can=Canvas(win)
# cord=10,50,200,100
# can.create_arc(cord,start=0,extent=200,fill="red")
# can.pack()

# Toplevel
top=Toplevel()
# top.pack()
l=Label(top,text="My Label",bg="black",fg="white", width="7",height="1")
l.pack()


# ProgressBar

def pro():
    pb['value']=30
    
    
pb=ttk.Progressbar(length=200)
pb.place(x=100,y=460)
bt=Button(text="Start",command=pro)
bt.place(x=130,y=490)

# Scrollbar

scrol=Scrollbar(win)
scrol.pack(side=RIGHT,fill=Y)

mylist=Listbox(win,yscrollcommand=Y)
scrol.config(command=mylist.yview)


for i in range(100):
    mylist.insert(END,i)

mylist.place(x=100,y=520)

# Menu
def demo():
    pass

def demo2():
    pass

my_menu=Menu(win)
win.config(menu=my_menu)

file_menu=Menu(my_menu)
edit_menu=Menu(my_menu)

my_menu.add_cascade(label="File",menu=file_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
my_menu.add_command(label="Format")
my_menu.add_command(label="View")
my_menu.add_command(label="Help")


file_menu.add_command(label="New",command=demo)
file_menu.add_command(label="New Window",command=demo)
file_menu.add_command(label="Open",command=demo)
file_menu.add_command(label="Save",command=demo)
file_menu.add_command(label="Save As",command=demo)
file_menu.add_separator()
file_menu.add_command(label="Page Setup",command=demo)
file_menu.add_command(label="Print",command=demo)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=demo)

edit_menu.add_command(label="cut",command=demo2)
edit_menu.add_command(label="Past",command=demo2)
edit_menu.add_command(label="Go To",command=demo2)


# PhotoImage

i=filedialog.askopenfilename(parent=win,initialdir=os.getcwd())
img=PhotoImage(file=i)

    
label=Label(win,image=img)
label.place(x=300,y=550,width=400,height=200)    
    
win.mainloop()