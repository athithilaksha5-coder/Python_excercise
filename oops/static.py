#instance specific method(object)
#static specific methods ----utility methods no self
#class specific methods
#--------------------------------------
#static methods
class Calculator:
	price = 100
	@staticmethod
	def add(no1,no2):
		print("welcome")
		print(Calculator.price)
		return no1+no2
		
		
	@staticmethod
	def sub(no1,no2):
		return no1-no2
		
calc = Calculator()
print(Calculator.add(100,50))
print(calc.sub(100,50))
		
		


