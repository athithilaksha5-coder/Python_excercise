class Parent:
	def a1(self):
		print("Parent a1")

class Child(Parent):
	def a1(self):
		print("Child a1")
		
class GChild(Child):
	def a1(self):
		print("GChild a1")
		
class GGChild(GChild):
	def a1(self):
		super().a1()
		print("GGChild a1")
	
class GGGChild(GGChild):
	def a1(self):
		GChild.a1(self)
		super().a1()
		print("gggchild")
		
		
ggg = GGGChild()
ggg.a1() 




