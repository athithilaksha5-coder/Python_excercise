no=int(input("Enter any number:"))
no1=no
def reverse(no,rev):
	if no>0:
		rem=no%10
		rev=rev*10+rem
		no=no//10
		reverse(no,rev)
	else:
		print(rev)
		print("palindrome" if rev==no1 else "Not a palindrome")
		
		
reverse(no,0)

		