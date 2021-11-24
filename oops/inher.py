#Inheritance:
#An object of one class behaving as an object of another class
#Manage Memory efficiently
#code reusalbility

class Parent():
	def add(self):
		print(10)
		
class Child(Parent):
	def sub(self):
		print(20)
		
class GrandChild(Child):
	def mul(self):
		print(30)
		
class Kinder(GrandChild):
	def div(self):
		print(40)
		
c = Kinder()
c.add()
c.sub()
c.mul()
c.div()
		