class Laptop:
	def __init__(self,brand,model,inches,price):
		self.brand = brand
		self.model = model
		self.inches = inches
		self.price = price
		
	def __str__(self):
		return "Brand_name:{}, Model:{}".format(self.brand,self.model)
	
lap1 = Laptop("Dell","inspiron",14,40000)
print(lap1)

	