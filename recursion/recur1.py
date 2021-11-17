def display(count,total):
	if count<=5:
		total =total+count
		print(count)
		count+=1
		display(count,total)
	else:
		print("Count of first five number is:",total)
		print("Average:",total/5)

display(1,0)