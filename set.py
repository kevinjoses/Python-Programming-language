# set
thisset={"apple","banana","cherry"}
print(thisset)

# duplicates not allowed
thisset={"apple","banana","cherry","apple"}
print(thisset)

# length of a set
thisset={"apple","banana","cherry"}
print(len(thisset))

# set items
set1={"apple","banana","cherry"}
set2={1,2,3,4}
set3={True,False,False}
print(set1)
print(set2)
print(set3)

# the set conductor
thisset=set(("apple","banana","cherry"))
print(thisset)

# set using for statement
thisset={"apple","banana","cherry"}
for x in thisset:
    print(x)

# access items in set
    
thisset={"apple","banana","cherry"}
print("banana"not in thisset)

# add items in set

thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

# add sets

thisset={"apple","banana","cherry"}
tropical={"pineapple","mango","cherry"}
thisset.update(tropical)
print(thisset)

# add any iterable

thisset={"apple","banana","cherry"}
mylist={"kiwi","orange"}
thisset.update(mylist)
print(thisset)

# remove set

thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

# discard

thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

# pop

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear

thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)

# delete

thisset={"apple","banana","cherry"}
del thisset
print(thisset)

# union

set1={"a","b","c"}
set2={1,2,3}

set3=set1.union(set2)
print(set3)