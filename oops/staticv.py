#Static variable
class School:
	fees = 100
	
	def __init__(self,sal):
		self.salary = sal
		
		
t1 = School(15000)
t2 = School(20000)
print(t1.salary, t1.fees)
print(t2.salary, t2.fees)
t1.fees = 150
t2.salary = 22000
print(t1.salary,t1.fees)
print(t2.salary,t2.fees)

