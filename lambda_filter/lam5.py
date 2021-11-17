tables = list(lambda i=i:i*10 for i in range(1,11))

for table in tables:
	print(table())
