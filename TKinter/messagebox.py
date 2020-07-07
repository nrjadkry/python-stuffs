from tkinter import *
from tkinter import messagebox

root=Tk()

root.title('MesageBox')

def popup():
	messagebox.showinfo("This is a popup","Hello World")
	messagebox.showwarning("This is a popup","Hello World")
	messagebox.showerror("This is a popup","Hello World")
	messagebox.askquestion("This is a popup","Hello World")
	messagebox.askokcancel("This is a popup","Hello World")
	messagebox.askyesno("This is a popup","Hello World")







mybutton=Button(root, text="Popup", command=popup,fg="blue",bg="yellow") #fg=foreground color i.e text color, bg=background color
mybutton.pack()



root.mainloop()
