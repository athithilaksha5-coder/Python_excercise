#method overroading

class Book:
	def __init__(self,pages):
		self.pages = pages
		
	def __add__(self,book2,book3):
		print(self.pages)
		return self.pages + book2.pages + book3.pages 
	
b1 = Book(300)
b2 = Book(200)
b3 = Book(300)

print(b1+b2+b3)