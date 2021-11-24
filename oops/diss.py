class school:
	def __init__(self,name='None',course='None',duration='None'):
		self.name=name
		self.course=course
		self.duration=duration
	def teaching(self):
		
		print(
self.name
)
	def centre(self):
		
		print(self.course)
	def classes(self):
		
		print(self.duration)
teacher1=school(name='payilagam',course='python',duration='2 months')
teacher2=school(name='payilagam',duration='1 months')


teacher1.teaching()
teacher1.centre()
teacher1.classes()
teacher2.teaching()
teacher2.centre()
teacher2.classes()

print(teacher1.__dict__)
print(teacher2.__dict__) 