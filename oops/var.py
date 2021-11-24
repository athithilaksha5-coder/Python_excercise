#Static variable

class School:
		
	def __init__(self,sal):
		School.fees=1000
		self.salary = sal
	
	#normal method
	def pay_fees(self,fee):
		School.late = 100
		self.examfee = fee
		
	@classmethod
	def prepare_rooms(cls):
		School.color = 'white'
		
	@staticmethod
	def abc():
		School.no = 5
		
		
		
		
t1 = School(15000)
t2 = School(20000)
print(t1.salary, t1.fees)
print(t2.salary, t2.fees)
t1.fees = 150
t2.salary = 22000
print(t1.salary,t1.fees)
print(t2.salary,t2.fees)




