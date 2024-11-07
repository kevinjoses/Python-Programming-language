# write a python program to create a set

thisset={"1,2,3,4,5"}
kevin=set(thisset)
print(type(kevin))

# write a python program to add members(s) to a set

thisset={3,4,5}
thisset.add(6)
print(thisset)

# write a python program to find common elements from to sets

a={"a","b","c"}
b={"d","e","f"}
a.intersection_update(b)
print(a)

# write a python program to compain two sets

a={"a","b","c"}
b={"1","2","3"}
c=a.union(b)
print(c)

# write a python program to create set difference

a={"a","b","c"}
b={"l","m","n"}
c=a.difference(b)
print(c)

# write a python program to check if a set is a subset of another set 

a={1,2,3,4,5,6,7}
b={1,2,3,9,10}
c=a.issubset(b)
print(c)

# write a python program to remove all elements from a given set

a={2,3,4,5,6,7,8,9}
a.clear()
print(a)

# write a python program to find the maximum and minimum value in a set

a={1,2,3,4}
b=max(a)
c=min(a)
print(a)
print(c)

# write a python program to check if a given value is present in set or not

a={1,2,3,4,5,6,7,8,9}
b=int(input("enter a digit:"))
c=b in a
if c:
    print("this value is present in the set",b)
else:
    print("this value not present in the set",b)

# write a python program to check if two given sets have no elements in common
    
a={1,2,3,4,5,6}
b={2,3,4,5}
c=a.issuperset(b)
print(c)

# write a python program to find elements in a given set that are not in another set

a={1,2,4,5,6}
b={7,8,9,5,10}
c=a-b
print(c)

a={"fast","spin","fitness","squeech"}
b=int(input("enter the number"))
c=[]
for i in range(b):
    l=input("enter a letter:")
    c.append(l)
    print(c)


