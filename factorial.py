def factorial(n):

	f=1
	for x in xrange(1,n+1):
		f=f*x
	return f

result=factorial(5)

print(result)