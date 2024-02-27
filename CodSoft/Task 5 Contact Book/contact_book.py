# Task No:5 Contact Book
#CodSoft

from tkinter import *
from tkinter import messagebox
import re
import pymysql
import tkinter as tk
from tkinter import ttk


host = 'localhost'
user = 'root'
password = ''

# Connect to MySQL server
try:
    con = pymysql.connect(host=host, user=user, password=password)
    cur = con.cursor()

    # Create the database (if it doesn't exist)
    cur.execute("CREATE DATABASE IF NOT EXISTS contact")

    # Use the database
    cur.execute("USE contact")

    # Create the 'cdata' table to store contact information
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cdata (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        number VARCHAR(10) NOT NULL,
        email VARCHAR(255),
        address VARCHAR(255)
    )
    """)

    print("Database and table created successfully.")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    if con:
        con.close()



root=tk.Tk()
root.maxsize(width=350,height=520)
root.minsize(width=350,height=520)

root.title("Contact Book")
label1=Label(text=" * My Contact Book *",font=('Helvetica 14 bold'),fg='red')
label1.place(x=83,y=20)


# --------- scrollbar -----------# 
frame2=ttk.Frame(root)

scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas=tk.Canvas(frame2,yscrollcommand=scrollbar.set,background='white')
inner_frame = Frame(canvas,bg='white')
canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

canvas.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)
canvas.config(scrollregion=canvas.bbox("all"))


def f1():
    frame1.place(x=35,y=150,width=280,height=350)
    frame2.place_forget()
    frame3.place_forget()
    
    
def f2():    
    canvas.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=canvas.bbox("all"))
    frame1.place_forget()
    frame3.place_forget()   
    frame2.update()
    frame2.update_idletasks()
    frame2.place(x=35,y=150,width=280,height=350)
    data=None
    i=None
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database='contact')
        cur=con.cursor()
        cur.execute("SELECT id,name,number FROM cdata")
        data=cur.fetchall()  
        con.commit()
        con.close()
        print(data)
        for i,(id,name,number) in enumerate(data, start=1):
            i=i*2
            print(i)
            l1 = tk.Label(inner_frame, text=f"Name: {name} ", font=('Helvetica 11 bold'), fg='black', bg='white')
            l1.grid(row=i * 2, column=0, padx=5, pady=10)
            l2 = tk.Label(inner_frame, text=f"Phone No: {number} ", font=('Helvetica 11 bold'), fg='black', bg='white')
            l2.grid(row=i * 2 + 1, column=0, padx=10, pady=5  )  
            
            bt1 = tk.Button(inner_frame, text=" Edit " , font=('Helvetica 10 bold'), fg='black', bg='yellow', width=5, height=1)
            bt1.grid(row=i * 2+2, column=0, sticky=tk.W, padx=5, pady=10)  
            bt1.bind("<Button-1>", lambda event, id={id}: edit(id))
            
            bt2 = tk.Button(inner_frame, text=" Delete ", font=('Helvetica 10 bold'), fg='white', bg='red', width=6, height=1)
            bt2.grid(row=i * 2+2, column=1, sticky=tk.W, padx=5, pady=10)
            bt2.bind("<Button-1>", lambda event, id={id}: delete_contact(id))
            
            l3=tk.Label(inner_frame,text="-----------/////-----------",bg='white',fg='black',height=-10)
            l3.grid(row=i * 2+3, padx=0, pady=0)
            # inner_frame.update_idletasks()
    except Exception as es:
        messagebox.showerror("Error",f"Error due to{str(es)}",parent=root) 
        
    
    
def f3():
    frame3.place(x=35,y=150,width=280,height=350)
    frame1.place_forget()
    frame2.place_forget()
    global ss
    global contact_id
    global i
    ss=search_entry.get()
    if(ss!=""):
        try:
            con2 = pymysql.connect(host='localhost', user='root', password='', database='contact')
            cur2 = con2.cursor()
            cur2.execute("SELECT id,name, number FROM cdata WHERE name LIKE %s OR number LIKE %s",
                        (f'%{ss}%', f'%{ss}%'))
            data2 = cur2.fetchall()
            con2.close()
            for i,(id,name,number) in enumerate(data2, start=1):
                i=i*2
                l11 = tk.Label(frame3, text=f"Name: "+str(name), font=('Helvetica 11 bold'), fg='black', bg='white')
                l11.grid(row=i * 2, column=0, padx=5, pady=10)
                
                l22 = tk.Label(frame3, text=f"Phone No: "+number, font=('Helvetica 11 bold'), fg='black', bg='white')
                l22.grid(row=i * 2 + 1, column=0, padx=10, pady=5 )  
                
                bt9 = tk.Button(frame3, text=" Edit " , font=('Helvetica 10 bold'), fg='black', bg='yellow', width=5, height=1)
                bt9.grid(row=i * 2+2, column=0, sticky=tk.W, padx=5, pady=10)  
                bt9.bind("<Button-1>", lambda event, id={id}: edit(id))
                
                bt10 = tk.Button(frame3, text=" Delete ", font=('Helvetica 10 bold'), fg='white', bg='red', width=6, height=1)
                bt10.grid(row=i * 2+2, column=1, sticky=tk.W, padx=5, pady=10)
                bt10.bind("<Button-1>", lambda event, id={id}: delete_contact(id))
                ss=None
                i=None
        except Exception as es:
            messagebox.showerror("Error", f"Error searching contacts: {str(es)}", parent=root)
    else:
        messagebox.showerror("Warning","Please enter Name or Number in Search Bar...")
        f2()
        
def delete_contact(contact_id):
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database='contact')
        cur=con.cursor()
        cur.execute("DELETE FROM cdata WHERE id = %s", (contact_id))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Contact Deleted")
        contact_id=None
        for widget in inner_frame.winfo_children():
            widget.destroy()
        f2()    
    except Exception as es:
        messagebox.showerror("Error", f"Error deleting contact: {str(es)}", parent=root)


# ----------------- HOME PAGE START-----------------#

bt5=Button(text="Add New Contact",font=('Helvetica 11 bold'),bg='orange',fg='white' ,command=f1)
bt5.place(x=20,y=70,width=132,height=31)

bt6=Button(text="View Contact List",font=('Helvetica 11 bold'),bg='orange',fg='white')
bt6.place(x=190,y=70,width=140)
bt6.bind("<Button-1>", lambda event : f2())


search_entry=Entry(root,font=('Helvetica 12'))
search_entry.place(x=60,y=115,width=160,height=25)

search_btn=Button(text="Search",font=('Helvetica 10 bold'))
search_btn.place(x=230,y=115,width=60,height=25)
search_btn.bind("<Button-1>", lambda event: f3())

# ----------------- HOME PAGE END-----------------#


# -------------- Frame1 Content START------------------- #
frame1=Frame(root,bg="white")

n=StringVar()

name=Label(frame1,text="Name:-",font=('Helvetica 11 bold'),fg='black',bg='white')
name.place(x=10,y=15)

nm=Entry(frame1,font=('Helvetica 11'),fg='black',highlightthickness=1,textvariable=n)
nm.place(x=10,y=40,width=220,height=25)

p=StringVar()
phone=Label(frame1,text="Phone No:-",font=('Helvetica 11 bold'),fg='black',bg='white')
phone.place(x=10,y=80)

ph=Entry(frame1,font=('Helvetica 11'),fg='black',highlightthickness=1,textvariable=p)
ph.place(x=10,y=110,width=220,height=25)

e=StringVar()
email=Label(frame1,text="Email Id:-",font=('Helvetica 11 bold'),fg='black',bg='white')
email.place(x=10,y=150)

em=Entry(frame1,font=('Helvetica 11'),fg='black',highlightthickness=1,textvariable=e)
em.place(x=10,y=180,width=220,height=25)

a=StringVar()
address=Label(frame1,text="Address:-",font=('Helvetica 11 bold'),fg='black',bg='white')
address.place(x=10,y=220)

ad=Entry(frame1,font=('Helvetica 11'),fg='black',highlightthickness=1,textvariable=a)
ad.place(x=10,y=250,width=220,height=25)


# -------------- Frame1 Content END------------------- #

# Modify the edit function to populate the "Add Contact" page for editing
def edit(edit_id):
    con = pymysql.connect(host='localhost', user='root', password='', database='contact')
    cur = con.cursor()
    cur.execute("SELECT name, number, email, address FROM cdata WHERE id = %s", (edit_id,))
    contact_data = cur.fetchone()
    con.close()
    f1()  # Show the "Add Contact" page for editing

    n.set(contact_data[0])  # Name
    p.set(contact_data[1])  # Phone Number
    e.set(contact_data[2])  # Email
    a.set(contact_data[3])  # Address

    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    pattern2 = r'^[a-zA-Z0-9._%+-]+@email\.com$'   
    if(n.get()==""):
        messagebox.showerror("Error","Please enter name")
    elif n.get().isdigit():
        messagebox.showerror("Error","Please enter valid name")
    elif(p.get()==""):
        messagebox.showerror("Error","Please enter number")
    elif not (p.get().isdigit()):
        messagebox.showerror("Error","Please enter valid number")    
    elif not(len(p.get())==10):
        messagebox.showerror("Error","Please enter valid number") 
    elif(e.get()==""):
        messagebox.showerror("Error","Please enter email")
    elif not(re.fullmatch(pattern,e.get()) or re.fullmatch(pattern2,e.get())):
        messagebox.showerror("Error","Please enter valid email")
    elif(a.get()==""):
        messagebox.showerror("Error","Please enter address")
        
    add2=Button(frame1,text="Update Contact",font=('Helvetica 11 bold'),fg='white',bg='green')
    add2.place(x=80,y=300,width=140,height=30)
    add2.bind("<Button-1>", lambda event, id={id}: up(n.get(),p.get(),e.get(),a.get(),edit_id))


def up(na,pa,ea,aa,edit_ida):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    pattern2 = r'^[a-zA-Z0-9._%+-]+@email\.com$'   
    if(na==""):
        messagebox.showerror("Error","Please enter name")
    elif na.isdigit():
        messagebox.showerror("Error","Please enter valid name")
    elif(pa==""):
        messagebox.showerror("Error","Please enter number")
    elif not (pa.isdigit()):
        messagebox.showerror("Error","Please enter valid number")    
    elif not(len(pa)==10):
        messagebox.showerror("Error","Please enter valid number") 
    elif(ea==""):
        messagebox.showerror("Error","Please enter email")
    elif not(re.fullmatch(pattern,ea) or re.fullmatch(pattern2,ea)):
        messagebox.showerror("Error","Please enter valid email")
    elif(aa==""):
        messagebox.showerror("Error","Please enter address")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='contact')
            cur = con.cursor()
            cur.execute("UPDATE cdata SET name=%s, number=%s, email=%s, address=%s WHERE id=%s",
                    (na, pa, ea, aa,edit_ida))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Contact Updated")
            edit_ida = None  # Reset the edit contact ID
            n.set("")
            p.set("")
            e.set("")
            a.set("")
            f2()
        except Exception as es:
            messagebox.showerror("Error", f"Error updating contact: {str(es)}", parent=root)     


def data():       
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    pattern2 = r'^[a-zA-Z0-9._%+-]+@email\.com$'   
    if(n.get()==""):
        messagebox.showerror("Error","Please enter name")
    elif n.get().isdigit():
        messagebox.showerror("Error","Please enter valid name")
    elif(p.get()==""):
        messagebox.showerror("Error","Please enter number")
    elif not (p.get().isdigit()):
        messagebox.showerror("Error","Please enter valid number")    
    elif not(len(p.get())==10):
        messagebox.showerror("Error","Please enter valid number") 
    elif(e.get()==""):
        messagebox.showerror("Error","Please enter email")
    elif not(re.fullmatch(pattern,e.get()) or re.fullmatch(pattern2,e.get())):
        messagebox.showerror("Error","Please enter valid email")
    elif(a.get()==""):
        messagebox.showerror("Error","Please enter address")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='contact')
            cur=con.cursor()
            cur.execute("insert into cdata (name,number,email,address) values (%s,%s,%s,%s)",
                        
                        (n.get(),
                         p.get(),
                         e.get(),
                         a.get() 
                        ))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Number Saved")
            n.set("")
            p.set("") 
            e.set("")  
            a.set("")   
            f2()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to{str(es)}",parent=root)


add=Button(frame1,text="Add Contact",font=('Helvetica 11 bold'),fg='white',bg='green')
add.place(x=80,y=300,width=100,height=30)
add.bind("<Button-1>", lambda event, id={id}: data())

frame3=Frame(root,bg='white')

root.mainloop()