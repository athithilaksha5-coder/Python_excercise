#Muthuramalingam says:Garbage Collection in Python 
#Aggregation in OOP - Python
#Composition in OOP - Python 

Aggregation in OOP - Python 

Composition in OOP - Python 
class College:
	def __init__(self,name):
		self.name = name
		self.lecturer = self.Dept()
		
	def admit(self):
		print('admission')
		
	class Dept:
		def __init__(self):
			pass
		
		def teach(self):
			print('teaching')
			
		def correction(self):
			print("paper correction")
			
			
s1 = College('raja')
s1.admit()
s1.lecturer.teach()
s1.lecturer.correction()
