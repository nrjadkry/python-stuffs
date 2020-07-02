def my_function():
	print("Hello")
	print("")

my_function()

#Arguments
def my_function(fname):
	print(fname+" Adhikari")
my_function("Niraj")
my_function("Niranjan")
my_function("Nischal")
print("")

#multiple arguments
def my_function(fname,lname):
	print(fname+" "+lname)

my_function("Niraj","Adhikari")

# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*name):
	print("Name: "+name[2])

my_function("Niraj","Niranjan","Nischal")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If you do not know how many keyword arguments that will be passed into your function, add two asterix: ** before the parameter name in the function definition.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("")#this is for extra space

#Default Parameter
#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


print("")#this is for extra space

#Passing a list as an argument

#if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print("")#this is for extra space

#Return value

#To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

