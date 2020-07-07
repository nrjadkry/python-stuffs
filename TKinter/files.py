from tkinter import *
from PIL import ImageTk, Image 

from tkinter import filedialog


root=Tk()

root.title('Files')


def openfiles():
	global myimage
	root.filename=filedialog.askopenfilename(initialdir='/home/Desktop',title="Select a file",filetypes=(('all files','*.*'),('png files','*.png')))
	mylabel=Label(root,text=root.filename).pack()

	myimage=ImageTk.PhotoImage(Image.open(root.filename))
	myimage_label=Label(image=myimage).pack()



mybtn=Button(root,text="Open Files",command=openfiles).pack()
mainloop()