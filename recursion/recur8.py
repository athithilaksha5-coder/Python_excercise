def fibo(i,f,s):
	if i<=10:
		print(f+s)
		s = f + s
		f = s - f
		i+=1
		fibo(i,f,s)
	
fibo(1,-1,1)
 	