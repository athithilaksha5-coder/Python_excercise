class School: 
#Whenever we create object, it will call constructors automatically

	def __init__(self,name,qual,exp):
		self.teacher  = name
		self.qual = qual
		self.exp = exp
		
	def teach(self):
		#self.teacher = "amala"
		print(self.teacher, 'is', end = ' ')
		print("Teaching to Students")
		
		
	def paperCorrection(self):
		#self.teacher = "amala"
		print(self.teacher, 'is', end = ' ')
		print("correcting papers")
		
	def conductExams(self):
		#self.teacher = "amala"
		print(self.teacher, 'is', end = ' ')
		print("conducting exams")
		
teacher = School("amala","M.A",6)
teacher2 = School("lakshmi","B.sc",3)
teacher.teach()
teacher.conductExams()
teacher.paperCorrection() 
teacher2.teach()
print(teacher2.qual)
print(teacher2.__dict__)
teacher2.conductExams()
