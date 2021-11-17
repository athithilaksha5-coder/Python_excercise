def check_prime(number,x):
	count = 0
	while x<number:
		if number%x==0:
			count+=1
		x+=1
	else:
		if count==0:
			return "prime number"
		else:
			return "not a prime number"
		
		
no=int(input("Enter any number"))
		
print(check_prime(no,2))
	