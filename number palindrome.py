number=int(input("input the number:"))
temp=number
rev=0
while number>0:
    r=number%10
    rev=rev*10+r
    number=number//10
print(temp)
if(temp==rev):
    print("this value is a palindrome number:")
else:
    print("this value is not a palindrome number:")
