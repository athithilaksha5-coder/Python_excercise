l = [10,10,10,10,10,20,20,30,30,30,40]
l1=set(l) #40,10,20,30
print(l1)
max=0
for i in l1:
	count=0
	for j in l:
		if i==j:
			count+=1
				
	else:
		print(i,"===>",count)
		if count>max:
			max=count
			result=i
else:
	print(result,"maximum count of elements in the list--",max)
		
		
		

	
		

	
	
	

		
		

		

			


		
		

		
	