# Python End Semester Project
# Name:- QR code generator for PDF

# all important packages

import time
import pyqrcode
import png
import cv2 as cv
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser
from fpdf import FPDF
import PyPDF2
from mega import Mega

f=1
while f>0:
	print("***** Create QR Code For PDF *****")
	print()
	print("1. Create your PDF File")
	print("2. Upload PDF File")
	print("3. Scan QR Code")
	print("4. Exit")
	print()
	time.sleep(5)

	# Taken one option from user
	n = int(input("Enter option number from above: "))
	print()
	# if user entered first option then execute below if condtion
	if n==1:#first option
	# ex. c:\file
		print("Enter full path where to save your PDF File ")
		p=input()
		# demo.pdf
		print()
		print("Enter PDF File Name ")
		name=input()
		name=name+".pdf"
		path2="/"
		path = "".join([p, path2, name])
		print()

		# Taken data from user
		nm=input("Enter full name: ")
		mobile=input("Enter mobile num: ")
		add=input("Enter Address: ")
		id=input("Enter id : ")
		# FPDF is a library for PDF document generation under Python
		pdf=FPDF()
		pdf.add_page()
		pdf.set_font("Arial",size=18)
		# set layout on page
		pdf.cell(100,40, txt=" PDF DATA ",ln=1,align="R")
		pdf.cell(20,10, txt="Name: "+nm,ln=1,align="L")
		pdf.cell(20,10, txt="Mobile Number: "+mobile,ln=1,align="L")
		pdf.cell(20,10, txt="Address: "+add,ln=1,align="L")
		pdf.cell(20,10, txt="id number: "+id,ln=1,align="L")
		pdf.output(path) #saving pdf file 
		print()
		# user details sending
		email = "vaidyarahul220@gmail.com"
		password = "Vaidya@220"
		mega = Mega()
		# login	
		m = mega.login(email, password)
		file = m.upload(path)
		url = m.get_upload_link(file)
		s=pyqrcode.create(url) #creating qrcode 
		imgpath1=".png" #saving it .png format
		x = name.split(".")
		imgpath = "".join([x[0], imgpath1])
		# set Qrcode image size
		s.png(imgpath,scale=8)
		print("Your PDF and QRcode created successful and store in entered location")
		time.sleep(7)
		print()

		# if user entered second option then execute below condition
	elif n==2:
	# Taken pdf file location from user
		print("Enter Your PDF File Path ")
		p=input()
		print()
		# Taken pdf name from user
		print("Enter Your PDF File Name ")
		name=input()
		path2="/"
		a=".pdf"
		path = "".join([p, path2, name,a])
		# user details
		email = "vaidyarahul220@gmail.com"
		password = "Vaidya@220"
		mega = Mega()
		# login
		m = mega.login(email, password)
		file = m.upload(path)
		url = m.get_upload_link(file)
		s=pyqrcode.create(url)
		imgpath1=".png"
		x = name.split(".")
		imgpath = "".join([x[0], imgpath1])
		s.png(imgpath,scale=8)
		print()
		print("Your PDF QRcode generated successful and store in entered location")
		time.sleep(5)

		print()
		# if user entered third option then execute below condition
	elif n==3:
		cap = cv.VideoCapture(0)
		while True:
			ret, frame = cap.read()
			AllQRObjects = pyzbar.decode(frame)
			for QR in AllQRObjects:
				print(QR.data.decode())
				url = QR.data.decode()
				print(url)
				webbrowser.open_new(url)
			cv.imshow('Window',frame)
			key = cv.waitKey(100)
			if key ==(ord('q')):
				break
				
		cv.destroyallWindows()
		cap.release()
		# break
		print('THE END')
	# when user enter fourth option then execute below code
	
	elif n==4:
		f=0
	else:
		print("Enter Valid option")