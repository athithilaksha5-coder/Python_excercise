	count = 0

	def digit(no):
		global count
		if no>0:
			no = no//10
			count+=1
			digit(no)
		return count

	no = int(input("Enter any digits:"))
	no1=no
	print("Count of digits by",no1,":",digit(no))
