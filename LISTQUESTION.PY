# write a python program to sum all the items in a list

x=[2,4,6,8]
sum=0
for i in x:
    sum+=i
print(("add all the numbers in the list"),sum)

# write a python program to multiply all the items in a list

x=[2,4,6,8,10]
multiply=1
for i in x:
    multiply*=i
print(("multplied value of the given list"),multiply)

# write a python program to get the largest number from the list

x=[2,4,6,8,10,12,14,16,18]
largestnumber=x[0]
for i in x:
    if i>largestnumber:
        largestnumber=i
print("largest number in the list is:",largestnumber)

# write a python program to get the smallest number from the list

x=[2,4,6,8,10,12,14,16,18]
smallestnumber=x[0]
for i in x:
    if i<smallestnumber:
        smallestnumber=i
print("smallest number in the list",smallestnumber)

# write a python program to remove duplicates from the list

x=[2,4,6,8,8,10,10,12,14,18,20]
y=[]
for i in x:
    if i not in (y):
        y.append(i)
print("new list",y)

# write a python program to check if a list is empty or not

x=[1,2,3,4,5,5,6,76,7,78,7,7,7,6,7,8,9]
if x==[]:
    print("list is empty")
else:
    print("list is not empty")

# write a python program to find the list of words that are longer than n from a given list of words
    
x=["kevin,hello,world"]
y=int(input("enter the number"))
word=[]
for i in x:
    if len(i)>y:
        word.append(i)
print(word)

# write a python program to create a list by concatenating a given list with 
# a range from 1 to n 
# sample list:['p','q']
# n=5
# sample output:['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']




