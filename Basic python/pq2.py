import pyqrcode
import png
import cv2 as cv
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser
from fpdf import FPDF
import PyPDF2
from mega import Mega



print("1.Create PDF File and Upload")
print("2.Upload PDF File")
print("3.Scan QR Code")
n = int(input())




if n==1:
    print("Enter Your PDF File Full Path For Save ")
    p=input()
    print("Enter Your PDF File Full Name ")
    name=input()
    #path1="./"
    path2="/"
    path = "".join([p, path2, name])
    name=input("full name:-")
    mobile=input("mobile num:-")
    addre=input("address:-")
    id=input("id number:-")
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=20)
    pdf.cell(100,40, txt="profile",ln=1,align="R")
    pdf.cell(20,10, txt="name:-"+name,ln=1,align="L")
    pdf.cell(20,10, txt="mobile:-"+mobile,ln=1,align="L")
    pdf.cell(20,10, txt="address:-"+addre,ln=1,align="L")
    pdf.cell(20,10, txt="id num:-"+id,ln=1,align="L")
    pdf.output(path)
    #print("pdf is successful store on your computer")
    # user details
    email = "vaidyarahul220@gmail.com"
    password = "Vaidya@220"
    mega = Mega()
    # login
    m = mega.login(email, password)
    file = m.upload(path)
    url = m.get_upload_link(file)
    #print(url)

    
    
    #s="Aniket";
    s=pyqrcode.create(url)
    imgpath1=".png"
    x = name.split(".")
    #print(x[0])
    imgpath = "".join([x[0], imgpath1])
            
    s.png(imgpath,scale=8)
    #print(url)

elif n==2:
    print("Enter Your PDF File Full Path ")
    p=input()
    print("Enter Your PDF File Full Name ")
    name=input()
    #path1="./"
    path2="/"
    path = "".join([p, path2, name])
    #print(path)
    # user details
    email = "vaidyarahul220@gmail.com"
    password = "Vaidya@220"
    mega = Mega()
    # login
    m = mega.login(email, password)
    
    file = m.upload(path)
    url = m.get_upload_link(file)
    #print(url)
    s=pyqrcode.create(url)
    imgpath1=".png"
    x = name.split(".")
    #print(x[0])
    imgpath = "".join([x[0], imgpath1])
    s.png(imgpath,scale=8)
    #print(url)

elif n==3:
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        AllQRObjects = pyzbar.decode(frame)
        for QR in AllQRObjects:
            print(QR.data.decode())
            url = QR.data.decode()
            print(url)
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(url)
            webbrowser.open_new(url)
            
        cv.imshow('Window',frame)
        key = cv.waitKey(100)
        if key ==(ord('q')):
            break
    cv.destroyAllWindows()
    cap.release()
    print('THE END')

    
else:
    print("Enter Valid option")
    

    

