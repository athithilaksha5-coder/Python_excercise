class Laptop:
	def __init__(self,brand,model, inches,price):
		self.brand = brand
		self.model = model
		self.inches = inches
		self.price = price
		
	def __str__(self): #Overriding
		return "Brand :{}, Model:{}".format(self.brand,self.model)
		
	
lap1 = Laptop("dell","Inspiron",14,40000)
print(lap1)
lap2 = Laptop("Lenovo","slim3",16,38000)
print(lap2)