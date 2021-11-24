class Vehicle:
	
	def __init__(self,name,max_speed=0,mileage=0):
		self.name=name
		self.speed = max_speed
		self.mile = mileage
		
	def get_data(self):
		print(f'Vehicle Name: {self.name}\nVehicle max_speed :{self.speed}\nMileage :{self.mile}')
		print("---------------------------")
		
		
vehicle1=Vehicle("Activa",180,40)
vehicle1.get_data()
vehicle2 = Vehicle("suzuki",160,45)
vehicle2.get_data()