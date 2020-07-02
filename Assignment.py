
test_list1 = [1, 4, 5] 
test_list2 = [3, 8, 9] 
  
# printing original lists 
print ("Original list 1 : " + str(test_list1)) 
print ("Original list 2 : " + str(test_list2)) 
  
# using map() + list comprehension 
# to interleave lists 
res = [i for j in map(None, test_list1, test_list2)   
                       for i in j if i is not None] 
  
# printing result 
print ("The interleaved list is : " + str(res)) 