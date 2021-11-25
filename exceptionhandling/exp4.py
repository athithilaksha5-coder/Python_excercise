#DEcarator 
#is a function which takes as a function and extern the function funatlitie

def decorator(fun): #fun represent display function
	def check(name,age):
		if name!='raja':
			print("welcome,",name)
			print("Your age is:",age)
		else:
			fun(name,age)
	return check


@decorator
def display(name,age):
	print("Hello,",name)
	print("Your age is,",age)
	
display('raja',25)
display('lakshmi',25)
	
