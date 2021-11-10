employee={"Madhan":50000,"Varun":35000,"Kumar":40000,"Arun":30000,"Arjun":35000}

sum=0
max=0
for k,v in employee.items():
	if k[0]=='A':
		print("Employee name start with 'A")
		print(k ,":", v)
			  
	if v>max:
		max=v
		result=k
	sum+=v
else:
	
	print("Highest salary employee in the dictionary:",k,":",max)
	print("sum of employees salary:",sum)



