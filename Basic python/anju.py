from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def init(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #first Image
        img=Image.open(r"C:\Users\kaleA\OneDrive\Desktop\FaceRecog\collage_images\standford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.Photoimage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
if _name_ ==  "_main_":
     root=Tk()
     obj=Face_Recognition_System()
     root.mainloop()