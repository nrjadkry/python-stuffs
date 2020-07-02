a=5
b=5

if a>b:
	print("a is gerater than b")
elif b>a:
	print("a is smaller than b")
else:
	print("a and b are equal")

	#print the boolean value
print(a<b) 
print(a>b)


if a==b: print("a and b are equal")

#And and or Operators
x=1
y=2
z=1

if x<y and y<z:
	print("x is the smallest")
else:
	print("x is not the smallest")

if x<y or x<z:
	print("Something")
else:
	print("Nothing")

#Nested if statement
m=125

if m>100:
	print("Greater than 100")
	if m>110:
		print("Greater then 110")
	else:
		print("Smaller then 110")
else:
	print("Smaller than 100")


#Pass statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

p=110
q=150

if p>q:
	pass

