from tkinter import *
from PIL import ImageTk, Image 

root=Tk()

root.title('First App')
# root.geometry("400x500")

myimg=ImageTk.PhotoImage(Image.open("Images/calculator.png"))
myimg1=ImageTk.PhotoImage(Image.open("Images/abc.png"))
myimg2=ImageTk.PhotoImage(Image.open("Images/chatbotlogo.png"))
myimg3=ImageTk.PhotoImage(Image.open("Images/logo.png"))
myimg4=ImageTk.PhotoImage(Image.open("Images/marcelo.jpg"))


ImageList=[myimg,myimg1,myimg2,myimg3,myimg4]



imagecounter=0

mylabel=Label(image=ImageList[imagecounter])
mylabel.grid(row=0,column=0,columnspan=3)

def forward():
	global imagecounter 
	print(len(ImageList))
	print(imagecounter)
	if imagecounter < (len(ImageList)-1):
		imagecounter += 1
		mylabel=Label(image=ImageList[imagecounter])
		mylabel.grid(row=0,column=0,columnspan=3)
	else:
		return


def back():
	global imagecounter 
	if imagecounter!=0:
		imagecounter -= 1
		mylabel=Label(image=ImageList[imagecounter])
		mylabel.grid(row=0,column=0,columnspan=3)



btn1=Button(root,text="<<",command=back).grid(row=1,column=0)
btn2=Button(root,text="Exit",fg="red",command=root.quit).grid(row=1,column=1)
btn3=Button(root,text=">>",command=forward).grid(row=1,column=2)


root.mainloop()