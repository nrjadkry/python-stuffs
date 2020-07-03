import tkinter
from tkinter import *

root=Tk()

root.title('First App')
root.geometry("400x500")



def hello():
	mylabel2=Label(root,text=mytextbox.get())
	mylabel2.pack()
	hello=mytextbox.get()
	print(hello)




mylabel=Label(root,text="Enter a name:")
mylabel.pack()

mytextbox=Entry(root, width=30)
mytextbox.pack()
mytextbox.insert(0,"Enter a a name")



mybutton=Button(root, text="Submit", command=hello,fg="blue",bg="yellow") #fg=foreground color i.e text color, bg=background color
mybutton.pack()



root.mainloop()

