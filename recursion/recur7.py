no1 = 12
no2 = 8

big = no1 if no1>no2 else no2


while True:
	if big%no1==0 and big%no2==0:
		print("LCM is ",big)
		break
	else:
		big+=1
		
