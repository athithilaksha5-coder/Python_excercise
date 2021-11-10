employee={"Madhan":50000,"Varun":35000,"Kumar":40000,"Arun":30000,"Arjun":35000}

for k,v in employee.items():
	employee[k]=employee.get(k)+500
else:
	print(employee)
	