from tkinter import *

root=Tk()

mylabel=Label(root,text="Enter a name:")
# mylabel.pack()

mylabel1=Label(root,text="Enter a name:")
# mylabel1.pack()

mylabel1.grid(row=0, column=1)
mylabel.grid(row=1,column=1)

# root.title('First App')
root.mainloop()
