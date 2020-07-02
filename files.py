f1=open("file1.txt","r")
f2=open("file2.txt","r")

data= f1.readlines()
# print(data)
data2=f2.readlines()
# print(data2)

if data==data2:
	print("They are Same files")
else:
	print("They are different")

	f1=open("file1.txt","r")
	f2=open("file2.txt","r")

	for line1 in f1:
	    for line2 in f2:
	        if line1==line2:
	            print("")
	        else:
	            print('FIrst line that is different of first file: '+ line1)
	            print('FIrst line that is different of that is different of second file: '+line2)
	        break
f1.close()
f2.close()