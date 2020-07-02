import re

text="I am hungry hahaha"

x=re.search("am",text)

if (x):
	print("Yes, We have a match")
else:
	print("No we dont have a match")

#display the position using start()
print(x.start())

#findall() diplay all the match
y=re.findall("h",text)
print(y)

#split() splits after the match
x=re.split("h",text)
print(x)

#split only in 1st occurance
x=re.split("h",text,1)
print(x)

#Sub replaces with other
x=re.sub('h','a',text)
print(x)

#replaces only in first 2 match
x=re.sub('h','a',text,2)
print(x)



str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object


#Searching an email in a text

text1="random String. helloAB@gmail.com. shjfdgs hasgf ghsd iam@hotmail122.com, nrjadkry@gmail.com, he-l.lo_hello@gmail.com niraj.adhikari@es.cloudfactory.com"
pattern=re.findall("[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9\.]+\.[a-zA-Z0-9]+",text1)

print(pattern)
