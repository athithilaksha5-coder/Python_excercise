class Math1:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def add(self):
		return self.x + self.y
	
	def sub(self):
		return self.x - self.y
	
	
class Math2:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def mul(self):
		return self.x * self.y
	
	def div(self):
		return self.x / self.y
	
	
class Math3:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.m1 = Math1(x,y)
		self.m2 = Math2(x,y)

	def power(self):
		return self.x ** self.y
	
	def add(self):
		return self.m1.add()
	
	def sub(self):
		return self.m1.sub()
	
	def mul(self):
		return self.m2.mul()
	
	
o = Math3(5,3)
print(o.add())
print(o.power())
print(o.mul())
