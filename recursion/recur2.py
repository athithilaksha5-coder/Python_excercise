def fact(count,total):
	if count<=no:
		total =total*count
		#print(count)
		count+=1
		fact(count,total)
	else:
		print("Count of first five number is:",total)
		
no=int(input("Enter any number:"))
fact(1,1)