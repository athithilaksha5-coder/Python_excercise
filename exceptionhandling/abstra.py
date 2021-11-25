class Library:
	def __init__(self,Books):
		self.BooksName=Books
	def List_Books(self):
		print("Available Books In Library")
		for names in self.BooksName:
			print(names)
		 
	def Borrow_Book(self,Borrow_Book):
		if Borrow_Book in self.BooksName:
			print("Get your book now")
			self.BooksName.remove(Borrow_Book)
		else:
			print("Book Not Available")
	def return_book(self,return_book):
		self.BooksName.add(return_book)
		print("You have returned the book!")
Books={'COBOL','c','c++','java','html','css','c#','javascript','Advanced java'}
obj=Library(Books)
msg="""
    1.Display Available Books
    2.Borrow Wanted Boook
    3.Return the Book
	0.Want to exit library
"""
option = True
while option:
	print(msg)
	try:
		choice=int(input("Enter the choice"))
		
		if choice==1:
			obj.List_Books()
		elif choice==2:
			books=input("enter the book name to borrow")
			obj.Borrow_Book(books)
		elif choice==3:
			books=input("enter the bookname to return")
			obj.return_book(books)
		elif choice ==0:
			print("Thank You!")
			option = False
	except:
		print("Please enter interger value")
		choice=int(input("Enter the choice"))
		
		if choice==1:
			obj.List_Books()
		elif choice==2:
			books=input("enter the book name to borrow")
			obj.Borrow_Book(books)
		elif choice==3:
			books=input("enter the bookname to return")
			obj.return_book(books)
		elif choice ==0:
			print("Thank You!")
			option = False


		
		