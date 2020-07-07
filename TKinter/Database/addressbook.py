from tkinter import *
from tkinter import filedialog
import sqlite3



root=Tk()

root.title('Address Book')
root.geometry("700x600")


#Databases


#Create a database or connet to the one
conn=sqlite3.connect('address_book.db')

#Creating a cursor
c=conn.cursor()

	

#Creating a table
'''
c.execute(""" CREATE TABLE addresses(
				first_name text,
				last_name text,
				address text,
				state text,
				city text,
				zipcode integer
	)

	""")
'''





#Submit Function
def submit():
	#Create a database or connet to the one
	conn=sqlite3.connect('address_book.db')

	#Creating a cursor
	c=conn.cursor()

	#Inserting data into database
	c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
		{
			'f_name':f_name.get(),
			'l_name':l_name.get(),
			'address':address.get(),
			'city':city.get(),
			'state':state.get(),
			'zipcode':zipcode.get(),


		})
		

	#Commit changes
	conn.commit()

	#Close connection
	conn.close()

	#Clearing the text boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)


def query():

	global frame


	frame=LabelFrame(root,padx=5, pady=5)
	frame.grid(row=8,column=0,padx=10,pady=10,columnspan=2)

	# Heading Labels for the data fetched
	heading_label_fname=Label(frame,text="First Name"+"\t", font='Helvetica 11 bold').grid(row=0,column=0)
	heading_label_lname=Label(frame,text="Last Name", font='Helvetica 11 bold').grid(row=0,column=1)
	heading_label_address=Label(frame,text="Address"+"\t", font='Helvetica 11 bold').grid(row=0,column=2)
	heading_label_city=Label(frame,text="City"+"\t", font='Helvetica 11 bold').grid(row=0,column=3)
	heading_label_state=Label(frame,text="State"+"\t", font='Helvetica 11 bold').grid(row=0,column=4)
	heading_label_zipcode=Label(frame,text="Zipcode"+"\t", font='Helvetica 11 bold').grid(row=0,column=5)
	heading_label_action=Label(frame,text="Action"+"\t", font='Helvetica 11 bold').grid(row=0,column=6)



	#Create a database or connet to the one
	conn=sqlite3.connect('address_book.db')

	#Creating a cursor
	c=conn.cursor()

	#Query the database
	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()

	#c.fetchone()
	#c.fetchmany(50)
	# print(records)

	# data=''
	# for record in records:
	# 	data +=str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + "\n"

	# data_label=Label(frame,text=data)
	# data_label.grid(row=9,column=0,columnspan=2)


	row=1

	for record in records:
		column=0
		# print(record[6])

		for i in range(len(record)-1):

			data_label=Label(frame,text=record[i])
			data_label.grid(row=row,column=column)

			column+=1

		
		action_frame=LabelFrame(frame)
		action_frame.grid(row=row,column=column)

		id=record[6]
		label_action=Button(action_frame,text="Delete", font='Helvetica 11 bold',fg="red",command=lambda id=id:delete(id))
		label_action.grid(row=0,column=0)

		button_edit=Button(action_frame,text="Edit", font='Helvetica 11 bold',fg="blue",command=lambda id=id:updateRecord(id))
		button_edit.grid(row=0,column=1)

		row+=1


	#Commit changes
	conn.commit()	
	#Close connection
	conn.close()


#Creating a function to delete a record
def delete(id):
	# print(id)
	#Create a database or connet to the one
	conn=sqlite3.connect('address_book.db')

	#Creating a cursor
	c=conn.cursor()

	#Delete Query
	c.execute("DELETE FROM addresses where oid="+str(id))
	frame.grid_forget()


	#Commit changes
	conn.commit()

	#Close connection
	conn.close()

	query()


def editRecord(id):
	#Create a database or connet to the one
	conn=sqlite3.connect('address_book.db')

	#Creating a cursor
	c=conn.cursor()
	record_id=id
	

	c.execute(""" UPDATE addresses SET 
		first_name = :f_name,
		last_name  = :l_name,
		address    = :address,
		city 	   = :city,
		state      = :state,
		zipcode    = :zipcode

		WHERE oid  = :oid """,

		{
			'f_name':f_name.get(),
			'l_name':l_name.get(),
			'address':address.get(),
			'city':city.get(),
			'state':state.get(),
			'zipcode':zipcode.get(),

			'oid':int(record_id)

		}

		)

	#Commit changes
	conn.commit()

	#Close connection
	conn.close()
	
	edit_window.destroy()
	root.deiconify()
	frame.grid_forget()
	query()






#Update Function
def updateRecord(id):
	# print(id)


	#Create a database or connet to the one
	conn=sqlite3.connect('address_book.db')

	#Creating a cursor
	c=conn.cursor()

	#Query the database
	c.execute("SELECT * FROM addresses where oid="+str(id))
	records=c.fetchall()

	# print(records)



	global edit_window
	#Creating text boxes
	edit_window=Tk()

	edit_window.title('Update Record')
	edit_window.geometry("700x600")

	global f_name 
	global l_name 
	global address 
	global city 
	global state 
	global zipcode 

	f_name=Entry(edit_window,width=30)
	f_name.grid(row=0,column=1,padx=10,pady=(10,0))

	l_name=Entry(edit_window,width=30)
	l_name.grid(row=1,column=1)

	address=Entry(edit_window,width=30)
	address.grid(row=2,column=1)

	city=Entry(edit_window,width=30)
	city.grid(row=3,column=1)

	state=Entry(edit_window,width=30)
	state.grid(row=4,column=1)

	zipcode=Entry(edit_window,width=30)
	zipcode.grid(row=5,column=1)

	# Creating labels for text boxes

	f_name_label=Label(edit_window,text="First Name :")
	f_name_label.grid(row=0, column=0, padx=140,pady=(10,0))

	l_name_label=Label(edit_window,text="Last Name :")
	l_name_label.grid(row=1, column=0)

	address_label=Label(edit_window,text="Address :")
	address_label.grid(row=2, column=0)

	city_label=Label(edit_window,text="City :")
	city_label.grid(row=3, column=0)

	state_label=Label(edit_window,text="State :")
	state_label.grid(row=4, column=0)

	zipcode_label=Label(edit_window,text="Zipcode :")
	zipcode_label.grid(row=5, column=0)

	#Creating submit Button

	btnsave=Button(edit_window,text="Save Data",command=lambda:editRecord(id))
	btnsave.grid(row=6,column=0,columnspan=2,padx=40,pady=10,ipadx=137)

	for record in records:
		f_name.insert(0,record[0])
		l_name.insert(0,record[1])
		address.insert(0,record[2])
		city.insert(0,record[3])
		state.insert(0,record[4])
		zipcode.insert(0,record[5])

	root.withdraw()






#Creating text boxes

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=10,pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

# Creating labels for text boxes

f_name_label=Label(root,text="First Name :")
f_name_label.grid(row=0, column=0, padx=140,pady=(10,0))

l_name_label=Label(root,text="Last Name :")
l_name_label.grid(row=1, column=0)

address_label=Label(root,text="Address :")
address_label.grid(row=2, column=0)

city_label=Label(root,text="City :")
city_label.grid(row=3, column=0)

state_label=Label(root,text="State :")
state_label.grid(row=4, column=0)

zipcode_label=Label(root,text="Zipcode :")
zipcode_label.grid(row=5, column=0)

#Creating submit Button

btnsubmit=Button(root,text="Submit",command=submit)
btnsubmit.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#creating query button
query_btn=Button(root,text="Show records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Commit changes
conn.commit()

#Close connection
conn.close()

mainloop()