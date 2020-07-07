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


status=Label(root,text="Image 1 of "+ str(len(ImageList)),bd=1,relief=SUNKEN, anchor=E) 
status.grid(row=3,column=0,columnspan=3,sticky=W+E)


def forward():
	global mylabel, status
	global imagecounter 
	global btn3
	if not imagecounter==(len(ImageList)-1):
		# print(imagecounter)
		mylabel.grid_forget()
	
		status.grid_forget()
		status=Label(root,text="Image "+ str(imagecounter+2) +" of "+ str(len(ImageList)),bd=1,relief=SUNKEN, anchor=E) 
		status.grid(row=3,column=0,columnspan=3,sticky=W+E)

	if imagecounter < (len(ImageList)-1):
		imagecounter += 1
		mylabel=Label(image=ImageList[imagecounter])
		mylabel.grid(row=0,column=0,columnspan=3)



def back():
	global imagecounter, status 
	global mylabel
	
	if not imagecounter==0:
		mylabel.grid_forget()

		status.grid_forget()
		status=Label(root,text="Image "+ str(imagecounter) +" of "+ str(len(ImageList)),bd=1,relief=SUNKEN, anchor=E) 
		status.grid(row=3,column=0,columnspan=3,sticky=W+E)

	# print(imagecounter)


	if imagecounter!=0:
		imagecounter -= 1
		mylabel=Label(image=ImageList[imagecounter])
		mylabel.grid(row=0,column=0,columnspan=3)




btn1=Button(root,text="<<",command=back,pady=2)
btn2=Button(root,text="Exit",fg="red",command=root.quit).grid(row=1,column=1)
btn3=Button(root,text=">>",command=forward, pady=2).grid(row=1,column=2)

btn1.grid(row=1,column=0)


root.mainloop()
