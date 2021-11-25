class Rocket:
	def __init__(self,name,distance):
		self.name = name
		self.distance = distance
		
	def launch(self):
		return "%s has reached %s" %(self.name,self.distance)
	
class MarsRover(Rocket):
	def __init__(self,name,distance,maker):
		Rocket.__init__(self,name,distance)
		self.maker = maker
		
	def get_maker(self):
		return "%s launched by %s" %(self.name,self.maker)
	
	def launch(self):
		print(super().launch())
		return self.name
	
	
	
x = Rocket("Simple rocket","till stratosphere")
y = MarsRover("Mars_rover","till mars","ISRO")
print(x.launch())
print(y.launch())
print(y.get_maker())


