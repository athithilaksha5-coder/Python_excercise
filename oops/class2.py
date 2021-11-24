class School:

	def __init__(self,**a):
		self.a=a

	def display(self):
		#self.teacher = "amala"
		for k,v in self.a.items():
			print(k ,": ",v)
		print("--------------------")

	
teacher1 = School(teachername="kavitha" ,qualification="bca",experience=2)
teacher2 = School(teachername="rani",experience=5)
teacher3 = School(teachername="valli")
teacher1.display()
teacher2.display()
teacher3.display() 