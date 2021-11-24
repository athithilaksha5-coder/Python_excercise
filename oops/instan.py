class Student:
	def __init__(self,name,grades):
		self.name = name
		self.grades = grades
		
	def average(self):
		return sum(self.grades)/len(self.grades)
	
	
student1 = Student("Rose",[56,85,75,65,90])

print(student1.name,",average mark is:",student1.average())