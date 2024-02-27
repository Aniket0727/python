# Assignment: Background remove
 
from rembg import remove 
from PIL import Image 
  
IP_img =  'F:nameLogo.png' 

OP_img = 'F:nameLogo_output.png' 
  
input = Image.open(IP_img) 
  
output = remove(input) 
  
if(output):
    print("Background removed succussfully...")
else:
    print("Background Not Remove") 
     
output.save(OP_img) 