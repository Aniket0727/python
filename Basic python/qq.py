import time
import pyqrcode
import png
import cv2 as cv
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser


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