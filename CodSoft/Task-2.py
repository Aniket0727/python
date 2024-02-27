# Task No:2 Calculator
#CodSoft

from tkinter import *

win=Tk()
win.minsize(width=305,height=322)

win.title("Calculator")

label2=Label(text="Calculator",bg="black",fg="white",width=22)
label2.config(font=('Fantasy 16 bold'))
label2.place(x=10,y=13)

label=Label(relief=SOLID,font=('Fantasy 14 bold'))
label.place(x=10,y=50,width=288,height=60)

equation=""

def show(value):
    global equation
    equation+=value
    label.config(text=equation)


def clear():
    global equation
    equation=" "
    label.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label.config(text=result)


# First Row

bt1=Button(text="C",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:clear())
bt1.place(x=10,y=120,width=65,height=33)

bt2=Button(text="/",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("/"))
bt2.place(x=85,y=120,width=65,height=33)

bt3=Button(text="%",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("%"))
bt3.place(x=160,y=120,width=65,height=33)

bt4=Button(text="*",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("*"))
bt4.place(x=235,y=120,width=65,height=33)


# Second Row

bt5=Button(text="7",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("7"))
bt5.place(x=10,y=160,width=65,height=33)

bt6=Button(text="8",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("8"))
bt6.place(x=85,y=160,width=65,height=33)

bt7=Button(text="9",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("9"))
bt7.place(x=160,y=160,width=65,height=33)

bt8=Button(text="-",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("-"))
bt8.place(x=235,y=160,width=65,height=33)


# Third Row

bt9=Button(text="4",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("4"))
bt9.place(x=10,y=200,width=65,height=33)

bt6=Button(text="5",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("5"))
bt6.place(x=85,y=200,width=65,height=33)

bt7=Button(text="6",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("6"))
bt7.place(x=160,y=200,width=65,height=33)

bt8=Button(text="+",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("+"))
bt8.place(x=235,y=200,width=65,height=33)


# Fourth Row

bt9=Button(text="1",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("1"))
bt9.place(x=10,y=240,width=65,height=33)

bt10=Button(text="2",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("2"))
bt10.place(x=85,y=240,width=65,height=33)

bt11=Button(text="3",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("3"))
bt11.place(x=160,y=240,width=65,height=33)

bt12=Button(text=" = ",bg='black',fg='white',font=('Cursive 14 bold'),command=calculate)
bt12.place(x=235,y=240,width=65,height=75)

bt13=Button(text="0",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("0"))
bt13.place(x=10,y=280,width=140,height=33)

bt14=Button(text=".",bg='black',fg='white',font=('Cursive 14 bold'),command=lambda:show("."))
bt14.place(x=160,y=280,width=65,height=33)


win.mainloop()