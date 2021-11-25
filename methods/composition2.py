class CountUp():
	def increment(self,num):
		self.counter = num + 1
		return self.counter
	
#c1 = CountUp()
#print(c1.increment(50))

class CountDown():
	def decrement(self,num):
		self.counter = num - 1
		return self.counter
	
#c2 = CountDown()
#print(c2.decrement(50))

class NewClass():
	def __init__(self,start = 0):
		self.counter = start
		self.cup = CountUp()
		self.cdown = CountDown()
		
	def increment(self):
		self.counter = self.cup.increment(self.counter)
	
	def decrement(self):
		self.counter = self.cdown.decrement(self.counter)
	
	def reset(self):
		self.counter = 0
		
	def getcount(self):
		return self.counter
	
c = NewClass()
print(c.increment())
print(c.increment())
print(c.getcount())

print(c.decrement())
print(c.getcount())

c1 = NewClass(50)
c1.increment()
c1.increment()
print(c1.getcount())
c1.decrement()
print(c1.getcount())
c1.reset()
print(c1.getcount())


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		