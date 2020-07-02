import os

#  This function creates a new file with a name 'info.txt'
# Try except is used to catch different errors.

def writeFile():


	try:
		file1=open('info.txt','w')
		file1.write("Hello")
	

	except IOError as error:
	 	print error
	except ValueError as ve:
	 	print ve
	except (ZeroDivisionError, NameError):
		print "\nError occured and handled"
	except SyntaxError as se:
		print 'Syntax Error'
	except RuntimeError as re:

		print 'Runtime error'
	except Exception as e:
		print 'Error'

	finally:
		# print 'File closed'
		file1.close()

#  This function opens a file with a name 'info.txt' if it exist.
# Try except is used to catch different errors.


def openFile():
	try:
		if os.path.exists("info.txt"):

	 		file1=open('info.txt','r')
	 	else:
	 		print 'File does not exist'
	 	# print file1.read()
	 	for data in file1:
	 		print data

	except IOError as error:
	 	print error
	except ValueError as ve:
	 	print ve
	except (ZeroDivisionError, NameError):
		print "\nError occured and handled"
	except SyntaxError as se:
		print 'Syntax Error'
	except RuntimeError as re:
		print 'Runtime error'
	except Exception as e:
		print 'Error'

	finally:
		# print 'File closed'
		file1.close()

# This function adds the data in the file if exists named "info.txt" if it is available. 
# Different types of possible errors are handled using try except error handling process. 
def appendFile():

	try:
		if os.path.exists("info.txt"):
			file1=open('info.txt','a')
			file1.write(" World!!")
		else:
			print 'File not found'

	except IOError as error:
	 	print error
	except ValueError as ve:
	 	print ve
	except (ZeroDivisionError, NameError):
		print "\nError occured and handled"
	except SyntaxError as se:
		print 'Syntax Error'
	except RuntimeError as re:
		print 'Runtime error'
	except Exception as e:
		print 'Error'

	finally:
		# print 'File closed'
		file1.close()

# This function deletes a file named "information.txt" if it is available. 
# Different types of possible errors are handled using try except error handling process. 
def deleteFile():
	try:			
		if os.path.exists("information.txt"):
			os.remove("information.txt")
			print("File deleted")

		else:
			print("File not found")

	except IOError as error:
	 	print error
	except ValueError as ve:
	 	print ve
	except (ZeroDivisionError, NameError):
		print "\nError occured and handled"
	except SyntaxError as se:
		print 'Syntax Error'
	except RuntimeError as re:
		print 'Runtime error'
	except Exception as e:
		print 'Error'

	finally:
		print ''



writeFile()

openFile()

appendFile()

deleteFile()

# 'information.txt file does not exist. If there was such a file then it would have been removed or deleted'