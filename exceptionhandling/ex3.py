# create Userdefined Exception 
class OldAgeException(Exception):
	def __init__(self,msg):
		self.msg = msg
		
age = int(input("Enter age:"))
try:
	if age>80:	
		#print("You are too old to travel")
		raise OldAgeException("You are too old to travel")
	
except OldAgeException:
	print("Seems not eligible")

print("HI")



	