Dict={}
print("Empty Dictionary: ")
print(Dict)

Dict={"Hello":"Greetings","Namaste":"Greetings in Nepali"}
print(Dict)

Dict={1:"Hello",2:"Namaste",3:"Thanks"}
print("\nDictionary with the use of Integer as keys: ")
print(Dict)

Dict={"Hello":"Greetings", 1:[1,2,3]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = dict({1: 'Hello', 2: 'Hi', 3:'Namaste'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Hello'), (2, 'Namaste')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


#Creating a nested Dictionary
Dict={1:"Hello",2:"Hi",3:{"A":"Hello","B":"Hi","C":"Welcome"}}
print("\n")
print(Dict) 

#Empty Dictionary
Dict={}
print("\nEmpty Dictionary")
print(Dict)

# Adding elements one at a time 
Dict[1]="Hello"
Dict[2]="Hi"
print("\nDictionary after adding elements: ") 
print(Dict)

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Hi'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 


# Python program to demonstrate   
# accesing a element from a Dictionary  
  
# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3))


# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict)

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict)


# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict)

# Deleting a Key  
# using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 

# Deleting an arbitrary Key-value pair 
# using popitem() 
Dict.popitem() 
print("\nPops an arbitrary key-value pair: ") 
print(Dict) 

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 

del Dict



Dict={1:"Hello",2:"Hi"}
print(Dict)

#Copying an entire dictionary
Dict2=Dict.copy()
print(Dict2)


#Get
print(Dict.get(1))

#Contacts can be stored in dictionary
contacts={"Niraj":"98601832666","Sudarshan":{"phone-no":"9865656465","email":"su@gmail.com"}}

print(contacts)


# print(contacts['Niraj'])

