class Calc:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		
	def add(self):
		return self.a+self.b
	
	def sub(self):
		return self.a-self.b
	
	def mul(self):
		return self.a*self.b
	
	def div(self):
		return self.a//self.b
	
	def mod(self):
		return self.a%self.b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
o = Calc(a,b)

while True:
	
	def option():
		print(f'0.Exit \n1.Addtion\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus')
		
	option()
	
	choice = int(input("Enter your choice"))
	print(choice)
	if choice ==1:
		
		print("Addition of given number:",o.add())
		print("--------------------")
			  
		
		
	elif choice==2:
		print("Subtraction of given number:",o.sub())
		print("--------------------")
		
		
	elif choice==3:
		print("Multiplication of given number:",o.mul())
		print("--------------------")
		
		
	elif choice==4:
		print("Division of given number:",o.div())
		print("--------------------")
		option()
		
	elif choice==5:
		print("Modulus of given number:",o.mod())
		print("--------------------")
	
		
	elif choice==0:
		print("exiting!!!!")
		break
	else:
		print("Invalid choice!!!!!!")
		break
		
		
		
		
	
				 
		