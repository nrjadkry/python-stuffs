list1=[1,2,3,4,5]
list2=['one','two','three','four','five']

zipped=list(zip(list1,list2))

print(zipped)


unzipped=list(zip(*zipped)) # * isused to unzip
print(unzipped)


goods=['apple','banana','cherry']
price=[0.5,0.6,0.7]
numbers=[2,5,8]

sentences=[]

for (goods,price,numbers) in zip(goods,price,numbers):
	goods,price,numbers=str(goods),str(price),str(numbers)
	new_sentence='I bought '+numbers+' '+goods+"'s at "+price
	sentences.append(new_sentence)

print(sentences)
	

