
nums=[3,2,4,5,6,7,8,9,10,12]

evens=list(filter(lambda n:n%2==0, nums)) #Use of filter
#lambda is aanonymous function

print(evens)

doubles=list(map(lambda n:n*2, evens))  #Use of map
print(doubles)