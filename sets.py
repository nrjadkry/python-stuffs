# enclosed in {}
# cannot have duplicates in set
# can grow and also get smaller
# its on order

set1 = {'banana','apple'} #set example

print(set1)

set1.add('cherry')

print(set1)

set1.add(4)
print(set1)

set1.add('banana') #it wont add banana again since it is already present


print(set1)

list_of_numbers=[1,1,2,3,4,4,5,'set','set','abc','abc']
print(list_of_numbers)
set_of_numbers=set(list_of_numbers)
print(set_of_numbers)

list_with_no_duplicates=list(set_of_numbers)
print(list_with_no_duplicates)
print("\n") #prints an empty line

#UNIONS
library_1={'Harry Porter','Lord of the rings','Romeo and Juliet','Hunger Games'}

library_2={'Harry Porter','Lord of the rings','Alchemist'}

all_books_in_town=library_1.union(library_2)
all_books_in_town2=library_1|library_2 #Union can also be done in this way

print("Union of a set")
print(all_books_in_town)
print(all_books_in_town2)
print("\n") #prints an empty line
#INTERSECTION
books_in_both_library=library_1.intersection(library_2)
books_in_both_library2=library_1 & library_2
print("intersection of a set")
print(books_in_both_library)
print(books_in_both_library2)

print("\n") #prints an empty line
#DIFFERENCES
books_only_in_library1=library_1-library_2
print(books_only_in_library1)

books_only_in_library2=library_2-library_1
print(books_only_in_library2)

print("\n") #prints an empty line

#Emptying the whole set
numbers={1,2,3,3,4}
print(numbers)
numbers.clear()
print(numbers)

print("\n") #prints an empty line

A=set()
B=set()

for i in range(1,10):
	A.add(i)

print('Set A =',A)
print("\n") #prints an empty line

set3={1,2,3,4,5}
set4={3,4,5,6,7,8,9}

set5=set3|set4
print("Union of Set3 & Set4: Set5 = ", set5) 
print("\n") #prints an empty line

set6=set3&set4
print("Intersection of set3 and set4: set6 =",set6)
print("\n") #prints an empty line

if set5>set6:
	print("Set 5 is superset of set 6")
elif set5<set6:
	print("Set 5 is subset ofset 6")
else:
	print("Set 5 and set 6 are same")

if set5.isdisjoint(set6):
	print("Set 5 and Set 6 have nothing in common")



