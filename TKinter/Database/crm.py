
from tkinter import *
from tkinter import filedialog
import mysql.connector
from tkinter import ttk
import csv



root=Tk()

root.title('CRM using MySql Db')
root.geometry("420x600")
root.resizable(False,False)

#Connect to mysql
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="N1r2j3**",
	database="crm",
	)

#Check to see if the connetion was created
# print(mydb)

#Creating a cursor and initailize it
my_cursor=mydb.cursor()

#Create a database
# my_cursor.execute("CREATE DATABASE  crm")

#Test if the database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
	# print(db)

#Create a table   **Back slash(\) is used to write the remaining code in another line
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers(first_name VARCHAR(255),\
											last_name VARCHAR(255),\
											zipcode INT(10),\
											price_paid DECIMAL(10,2),\
											user_id INT AUTO_INCREMENT PRIMARY KEY)")
#IF NOT EXISTS checks if the exists or not. If does not exist it creates another. 

#Show tables
# my_cursor.execute("SELECT * from customers")
# print(my_cursor.description)

#Drop Table
# my_cursor.execute("DROP TABLE customers")

#Alter table
'''
my_cursor.execute("ALTER TABLE customers ADD(email VARCHAR(255),\
												address VARCHAR(255),\
												city VARCHAR(50),\
												state VARCHAR(50),\
												country VARCHAR(255),\
												phone VARCHAR(255),\
												payment_method VARCHAR(50),\
												discount_code VARCHAR(255)\
												)")
'''

# Clear Text Fields
def clear_fields():
	first_name_box.delete(0, END)
	last_name_box.delete(0, END)
	address_box.delete(0, END)
	city_box.delete(0, END)
	state_box.delete(0, END)
	zipcode_box.delete(0, END)
	country_box.delete(0, END)
	phone_box.delete(0, END)
	# username_box.delete(0,END)
	email_box.delete(0, END)
	payment_method_box.delete(0, END)
	discount_code_box.delete(0, END)
	price_paid_box.delete(0, END)

def add_customer():

	sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
	my_cursor.execute(sql_command, values)

	# Commit the changes to the database
	mydb.commit()
	print('Data inserted')
	# Clear the fields
	clear_fields()

def export_to_csv(result):
	with open('customers.csv','a',newline="") as f:
		w=csv.writer(f,dialect='excel')
		for record in result:
			w.writerow(record)



def show_customers():
	show_data_window=Tk()

	show_data_window.title('Customer Details')
	show_data_window.geometry("1000x400")

	def search_data():
		frame_for_data.grid_forget()
		labels_for_customers()
		last_name=search_box.get()
		selected=dropdown_Search.get()
		sql=""
		if selected == "Search by..":
			result="Select an option from dropdown"
			label_data=Label(frame_for_data,text=result,font="Helvetica, 14",fg="blue")
			label_data.grid(row=3,column=0,columnspan=3,padx=15)
			
		if selected == "First Name":
			sql="SELECT * FROM customers WHERE first_name = %s"
		if selected == "Last Name":
			sql="SELECT * FROM customers WHERE last_name = %s"
		if selected == "Customer Id":
			sql="SELECT * FROM customers WHERE user_id = %s"
		if selected == "Email":
			sql="SELECT * FROM customers WHERE email = %s"
				

		if not selected=="Search by..":

			name=(last_name,)
			data=my_cursor.execute(sql,name)
			data=my_cursor.fetchall()
			if not data:
				result="No Records found"
				label_data=Label(frame_for_data,text=result,font="Helvetica, 14",fg="red")
				label_data.grid(row=3,column=0,columnspan=3,padx=15)
			else:

				# print(data)

			
				for index,d in enumerate(data):
					col=0

					for x in d:

						# print(d[4])

						label_data=Label(frame_for_data,text=x)
						label_data.grid(row=index+2,column=col)
						col+=1 




	#Search by Last Name Label
	# search_label=Label(show_data_window,text="Last Name").grid(row=0,column=0,sticky=E)

	#Dropdown box with ttk
	dropdown_Search=ttk.Combobox(show_data_window,values=["Search by..","Last Name","First Name","Email","Customer Id"])
	dropdown_Search.current(0)
	dropdown_Search.grid(row=0,column=0,sticky=E)

	#Last Name text box
	search_box=Entry(show_data_window)
	search_box.grid(row=0,column=1)
	
	#Search Button
	search_button=Button(show_data_window,text="Search",command=search_data)
	search_button.grid(row=0,column=2,sticky=W)
	# last_name=search_box.get()


	global labels_for_customers
	def labels_for_customers():
		global frame_for_data

		frame_for_data=LabelFrame(show_data_window,padx=5, pady=5)
		frame_for_data.grid(row=1,column=0,padx=10,pady=10,columnspan=3)

		first_name_label=Label(frame_for_data,text="First Name",font="Helvetica, 11").grid(row=1,column=0,sticky=W,padx=5,pady=10)
		last_name_label=Label(frame_for_data,text="Last Name",font="Helvetica, 11").grid(row=1,column=1,sticky=W)
		address_label=Label(frame_for_data,text="Zipcode",font="Helvetica, 11").grid(row=1,column=2,sticky=W,padx=5)
		country_label=Label(frame_for_data,text="Price Paid",font="Helvetica, 11").grid(row=1,column=3,sticky=W,padx=5)
		city_label=Label(frame_for_data,text="User Id",font="Helvetica, 11").grid(row=1,column=4,sticky=W,padx=5)
		email=Label(frame_for_data,text="Email",font="Helvetica, 11").grid(row=1,column=5,padx=5)
		zipcode_label=Label(frame_for_data,text="Address",font="Helvetica, 11").grid(row=1,column=6,sticky=W,padx=5)
		phone_label=Label(frame_for_data,text="City",font="Helvetica, 11").grid(row=1,column=7,sticky=W,padx=5)
		state_label=Label(frame_for_data,text="State",font="Helvetica, 11").grid(row=1,column=8,sticky=W,padx=5)
		country_label=Label(frame_for_data,text="Country",font="Helvetica, 11").grid(row=1,column=9,sticky=W,padx=5)
		phone_label=Label(frame_for_data,text="Phone No",font="Helvetica, 11").grid(row=1,column=10,sticky=W,padx=5)
		payment_method_label=Label(frame_for_data,text="Payment Method",font="Helvetica, 11").grid(row=1,column=11,sticky=W,padx=5)
		discount_code_label=Label(frame_for_data,text="Discount Code",font="Helvetica, 11").grid(row=1,column=12,sticky=W,padx=5)
		action_label=Label(frame_for_data,text="Action",font="Helvetica, 11").grid(row=1,column=13,sticky=W,padx=5)

	labels_for_customers()
	my_cursor.execute("SELECT * FROM customers")
	data=my_cursor.fetchall()
	# print(data)

	def updateData(id):
		show_data_window.destroy()

		update_data_window=Tk()

		update_data_window.title('Update Customer Data')
		update_data_window.geometry("500x600")

		customer_data_labels(update_data_window)

		# def update_customer(id):
		sql="SELECT * FROM customers WHERE user_id = %s"
		name=(id,)
		data=my_cursor.execute(sql,name)
		data=my_cursor.fetchall()
		# print(data)


		first_name_box.insert(0,data[0][0])
		last_name_box.insert(0,data[0][1])
		zipcode_box.insert(0,data[0][2])
		price_paid_box.insert(0,data[0][3])
		email_box.insert(0,data[0][5])
		address_box.insert(0,data[0][6])
		city_box.insert(0,data[0][7])
		state_box.insert(0,data[0][8])
		country_box.insert(0,data[0][9])
		phone_box.insert(0,data[0][10])
		payment_method_box.insert(0,data[0][11])
		discount_code_box.insert(0,data[0][12])

			
		def update_customer(id):
			sql_command=""" UPDATE customers SET first_name=%s, last_name=%s, address=%s,email=%s,zipcode=%s,city=%s,state=%s,country=%s,\
			phone=%s,payment_method=%s,discount_code=%s,price_paid=%s WHERE user_id=%s """


			first_name=first_name_box.get()
			last_name=last_name_box.get()
			address=address_box.get()
			zipcode=zipcode_box.get()
			email=email_box.get()
			city=city_box.get()
			state=state_box.get()
			country=country_box.get()
			phone=phone_box.get()
			payment_method=payment_method_box.get()
			discount_code=discount_code_box.get()
			price_paid=price_paid_box.get()


			inputs=(first_name,last_name,address,email,zipcode,city,state,country,phone,payment_method,discount_code,price_paid,id)

			my_cursor.execute(sql_command,inputs)
			mydb.commit()

			update_data_window.destroy()
			# frame_for_data.grid_forget()
			show_customers()




		update_customer_button = Button(update_data_window, text="Update Data",command=lambda:update_customer(id))
		update_customer_button.grid(row=14, column=0, padx=10, pady=10)
		

	
	for index,d in enumerate(data):
		col=0

		for x in d:

			# print(d[4])

			label_data=Label(frame_for_data,text=x)
			label_data.grid(row=index+2,column=col)
			col+=1 
			id=d[4]
		button_edit=Button(frame_for_data,text="Edit", font='Helvetica 11 bold',fg="blue",command=lambda id=id:updateData(id))
		button_edit.grid(row=index+2,column=col)



	export_button=Button(show_data_window,text="Export to CSV",command=lambda:export_to_csv(data))
	export_button.grid(row=2,column=0,padx=15,pady=10)



#Create lables
title_label=Label(root,text="CRM Database",font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,pady=10,sticky=W)

#Create Main Form
def customer_data_labels(root):
	first_name_label=Label(root,text="First Name").grid(row=1,column=0,sticky=W,padx=10,pady=5)
	last_name_label=Label(root,text="Last Name").grid(row=2,column=0,sticky=W,padx=10)
	address_label=Label(root,text="Address").grid(row=3,column=0,sticky=W,padx=10)
	country_label=Label(root,text="Country").grid(row=4,column=0,sticky=W,padx=10)
	city_label=Label(root,text="City").grid(row=5,column=0,sticky=W,padx=10)
	state_label=Label(root,text="State").grid(row=6,column=0,sticky=W,padx=10)
	zipcode_label=Label(root,text="Zipcode").grid(row=7,column=0,sticky=W,padx=10)
	phone_label=Label(root,text="Phone No").grid(row=8,column=0,sticky=W,padx=10)
	email_label=Label(root,text="Email").grid(row=9,column=0,sticky=W,padx=10)
	# username_label=Label(root,text="Username").grid(row=10,column=0,sticky=W,padx=10)
	payment_method_label=Label(root,text="Payment Method").grid(row=11,column=0,sticky=W,padx=10)
	discount_code_label=Label(root,text="Discount Code").grid(row=12,column=0,sticky=W,padx=10)
	price_paid_label=Label(root,text="Price Paid").grid(row=13,column=0,sticky=W,padx=10)

	global first_name_box, last_name_box, address_box, country_box, city_box, state_box, zipcode_box,phone_box,email_box,payment_method_box,discount_code_box,price_paid_box
	#Create Entry Box
	first_name_box=Entry(root)
	first_name_box.grid(row=1,column=1)

	last_name_box=Entry(root)
	last_name_box.grid(row=2,column=1,pady=5)

	address_box=Entry(root)
	address_box.grid(row=3,column=1,pady=5)

	country_box=Entry(root)
	country_box.grid(row=4,column=1,pady=5)

	city_box=Entry(root)
	city_box.grid(row=5,column=1,pady=5)

	state_box=Entry(root)
	state_box.grid(row=6,column=1,pady=5)

	zipcode_box=Entry(root)
	zipcode_box.grid(row=7,column=1,pady=5)

	phone_box=Entry(root)
	phone_box.grid(row=8,column=1,pady=5)

	email_box=Entry(root)
	email_box.grid(row=9,column=1,pady=5)

	# username_box=Entry(root)
	# username_box.grid(row=10,column=1,pady=5)

	payment_method_box=Entry(root)
	payment_method_box.grid(row=11,column=1,pady=5)

	discount_code_box=Entry(root)
	discount_code_box.grid(row=12,column=1,pady=5)

	price_paid_box=Entry(root)
	price_paid_box.grid(row=13,column=1,pady=5)


customer_data_labels(root)

# Create Buttons
add_customer_button = Button(root, text="Add Customer To Database",command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)
clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)
show_data_button=Button(root,text="Show Customers",command=show_customers)
show_data_button.grid(row=15,column=0)

mainloop()