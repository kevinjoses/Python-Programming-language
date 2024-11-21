# write a python program to find out a given nmber is pallindrome or not

num=1634
order=len(str(num))
sum=0
temp=num
while num>0:
    r=temp%10
    sum+=r**order
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
