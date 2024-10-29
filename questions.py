# Q1  # Write a python program to get a string from a given string where all occurences of its first char have 
    # been changed to $ except the first char itself
    # sample string:'restart'
    # excepted result:'resta$te$'

# Q5   # Write a python script that takes input from the user and displays that input back in upper and lower
     # cases

a=input("enter a string:")
print("upper case:",a.upper())
print("lower case:",a.lower())

# Q2  Write a python program to reverse a string
a="kevin jose"
reversedstring=a[::-1]
print(reversedstring)

# Q3  Write a python program to remove characters that have odd index values in a given string
a="96594365493785695837 kevin"
result=''
i=0
while i<len(a):
    if i%2==0:
        result+=a[i]
    i+=1
print("modified string:",result)

# Q8 Write a python program to count repeated characters in a string 
# sample string:'thequickbrownfoxjumpsoverthelazydog'
# expected output:
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


txt='thequickbrownfoxjumpsoverthelazydog'
x=txt.count("o")
a=txt.count("e")
print("o",x)
print("e",a)

