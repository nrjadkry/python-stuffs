days=["Sunday","Monday","Tuesday"]
for x in days:
	print(x)

for y in "Wed":
	print(y)

#break statement
for x in days:
	print(x)
	if x=="Monday":
		break

	
#continue statement
fruits=["Apple","Banana","Grapes"]
for x in fruits:
	if x=="Banana":
		continue
	print(x)

#range
for x in range(5):
	print(x) #range starts from 0 and ends at the number increasing by 1

for x in range(9,13):
	print(x)

#range starts from first parameter till the last parameter increasing by the third parameter
for x in range(5,10,2):
	print(x)


for x in xrange(1,3):
	print(x)
else:
	print("Finished")
	print("")

#Nested Loop

days=["Sunday","Monday","Tuesday"]

fruits=["Apple","Banana","Grapes"]

for x in days:
	for y in fruits:
		print (x,y)

#Pass statement
for x in xrange(1,10):
	pass