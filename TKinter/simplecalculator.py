from tkinter import *

root=Tk()


root.title('Calculator')
# root.iconbitmap('/home/calculator.ico')
root.resizable(0,0)




mytextbox=Entry(root, borderwidth=5)
mytextbox.grid(row=0,column=0,columnspan=4)


def btn_click(n):
	m=mytextbox.get()
	mytextbox.delete(0,END)
	mytextbox.insert(0,m+str(n))
	# mytextbox.insert(0, n)
def btn_clear():
	mytextbox.delete(0,END)

def add():
	first_no=float(mytextbox.get())
	global f_num, operation
	f_num=first_no
	operation="ADD"
	mytextbox.delete(0,END)

def substract():
	first_no=float(mytextbox.get())
	global f_num
	f_num=first_no
	global operation
	operation="SUB"
	mytextbox.delete(0,END)

def multiply():
	first_no=float(mytextbox.get())
	global f_num
	f_num=first_no
	global operation
	operation="MUL"
	mytextbox.delete(0,END)

def divide():
	first_no=float(mytextbox.get())
	global f_num
	f_num=first_no
	global operation
	operation="DIV"
	mytextbox.delete(0,END)



def equal():
	second_no=float(mytextbox.get())
	if operation == "ADD":
		result=f_num+second_no
	elif operation=="SUB":
		result=f_num-second_no
	elif operation=="MUL":
		result=f_num*second_no
	elif operation=="DIV":
		result=f_num/second_no

	mytextbox.delete(0,END)
	mytextbox.insert(0,result)




# btn1=Button(root, text="=",fg="blue",bg="yellow").grid(row=1,column=0)

btn1=Button(root,padx=15,pady=5, text="9",command=lambda: btn_click(9)).grid(row=1,column=0)
btn2=Button(root,padx=15,pady=5, text="8",command=lambda: btn_click(8)).grid(row=1,column=1)
btn3=Button(root,padx=15,pady=5, text="7",command=lambda: btn_click(7)).grid(row=1,column=2)
btn4=Button(root,padx=15,pady=5, text="+",command=add).grid(row=1,column=3)

btn5=Button(root,padx=15,pady=5, text="6",command=lambda: btn_click(6)).grid(row=2,column=0)
btn6=Button(root,padx=15,pady=5, text="5",command=lambda: btn_click(5)).grid(row=2,column=1)
btn7=Button(root,padx=15,pady=5, text="4",command=lambda: btn_click(4)).grid(row=2,column=2)
btn8=Button(root,padx=15,pady=5, text="-",command=substract).grid(row=2,column=3)

btn9=Button(root,padx=15,pady=5, text="3",command=lambda: btn_click(3)).grid(row=3,column=0)
btn10=Button(root,padx=15,pady=5, text="2",command=lambda: btn_click(2)).grid(row=3,column=1)
btn11=Button(root,padx=15,pady=5, text="1",command=lambda: btn_click(1)).grid(row=3,column=2)
btn12=Button(root,padx=15,pady=5, text="x",command=multiply).grid(row=3,column=3)

btn13=Button(root,padx=15,pady=5, text="%").grid(row=4,column=0)
btn14=Button(root,padx=15,pady=5, text="0",command=lambda: btn_click(0)).grid(row=4,column=1)
btn15=Button(root,padx=15,pady=5, text=".",command=lambda: btn_click(".")).grid(row=4,column=2)
btn16=Button(root,padx=15,pady=5, text="/",command=divide).grid(row=4,column=3)


btn17=Button(root,padx=15,pady=5, text="C",command=btn_clear).grid(row=5,column=0,columnspan=2)
btn18=Button(root,padx=15,pady=5, text="=",command=equal).grid(row=5,column=2,columnspan=2)
# btn1=Button(root, text="",fg="blue",bg="yellow").grid(row=5,column=2,columnspan=2)



root.mainloop()