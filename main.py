n=input("enter Number")
'''l=len(n)
for i in range(l//2):
	if(n[i]!=n[l-i-1]):
		print("Not a palindrome")
		i=0	
		break
if(i!=0):
	print("It is a palindrome")'''


if(n==n[::-1]):
	print("It is Pali")
else:
	print("Not a Palindrome")


		
	