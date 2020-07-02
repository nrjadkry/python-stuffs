
def fibonacci(n):
	a=0
	b=1

	if n<0:
		print("Provide a valid number")
	elif n==0:
		print(0)
	else:


		if n==1:
			
			print(a)

		else:
			print(a)
			print(b)
			for x in xrange(n-2):
				

				c=a+b
				if c<n:
					print(c)
					a=b
					b=c


fibonacci(10) # Display all the fibonacci numbers less than 100
