def prime(no,i):
	if no>1:
		if i<no:
			if no%i!=0:
				i+=1
				prime(no,i)
			else:
				print(no,",is not a prime number")
		else:
			print(no,",is a prime number")
	
		
			
	else:
		print(no,",is not a prime number")
		
		
number=int(input("Enter any number:"))

prime(number,2)