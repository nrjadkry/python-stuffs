name=['Niraj','Niranjan','Nischal']

l=[]
for person in name:
	l.append(person)
print(l)

#list comprehension
print([person for person in name])

l=[]
for person in name:
	l.append(person+' dumped her')
print(l)

#list comprehension
print([person+' dumped her.' for person in name])

movies_ratings={'Interstellar':9,'Dark Knight':8,'Persuit of Happiness':10,'Hello':2}

l=[]
for movie in movies_ratings:
	if movies_ratings[movie]>5:
		l.append(movie)

print(l)

#Using list comprehension
print([movie for movie in movies_ratings if movies_ratings[movie]>5])

#Divisible by 2

numbers={1,2,3,4,5,6,8,9,12,13}

l=[]

for no in numbers:
	if no % 2==0:
		l.append(no)
print(l)

#Using list comprehension
print([no for no in numbers if no % 2==0])

#All the numbers from 1 to 10 multiply by 2
list2=[]
for numbers in xrange(1,10):
	list2.append(numbers*2)
print(list2)

#Using list comprehension
print([numbers*2 for numbers in range(1,10) ])
