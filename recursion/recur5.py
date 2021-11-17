a = 0
def addition(no):
	global a
	if no>0:
		rem=no%10
		a=a+rem
		no=no//10
		addition(no)
	return a

no = int(input("Enter any number:"))
print("addition of",no,"is",addition(no))
	