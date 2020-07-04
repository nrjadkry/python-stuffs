#1,1,2,3,5,8,13,21,........100th
#a b a+b
#  a  b  a+b
def fibonacci(n):

	if n==0:
		print(0)
	elif n==1:
		print(1)
	elif n<0:
		print('Provide a valid number')

	else:
		a=1
		b=1

		print(a)
		print(b)
		
		for m in range(n):
			
			x=a+b 
			if x<=n: 
				print(x)
			a=b
			b=x



# hhh = input("Enter your value: ") 
# try:
# 	fibonacci(int(hhh))
# except ValueError:
# 	print('Provide a valid number')

def split(word): 
    return [char for char in word]  
      
# Driver code 
word = 'geeks'
print(split(word))
