from datetime import date

class Person:
	
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	#create a class method 
	@classmethod
	def fromBirthYear(cls,name,year):
		return Person(name,date.today().year - year)
		#return cls(name,date.today().year - year)
		
	# create a static method
	@staticmethod
	def isAdult(age):
		return age > 18
		
		
person1 = Person("rajan" , 21)
person2 = Person.fromBirthYear("rajan",1995)

print(person1.age)
print(person2.age)

print(Person.isAdult(23))



