# write a python program to convert a tuple to a string

x=("apple","banana","cherry",)
y=",".join(x)
print(y)

# write a python program to find repeated items in a tuple

x=("apple","banana","banana","strawberrry",)
counts=[]
for i in x:
    if x.count(i)>1:
        if i not in counts:
            counts.append(i)
print("repeated",counts)

# write a python program to check whether an element exists within a tuple

names=("emmanual","kevin","smera","smera")
smera=(input("enter your element:"))
if smera in names:
    print(f"yes",{smera})
else:
    print(f"no",{smera})

