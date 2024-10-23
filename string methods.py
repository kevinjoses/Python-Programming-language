# captilize
txt="hello, my name is kevin."
x=txt.capitalize()
print(x)

# casefold
txt="Hello, My Name Is Kevin."
x=txt.casefold()
print(x)

# center
txt="kevin"
x=txt.center(20)
print(x)

# count
txt="My name is kevin."
x=txt.count("kevin")
print(x)

# encode
txt="My name is kevin."
x=txt.encode()
print(x)

# endswith
txt="My name is kevin."
x=txt.endswith(".")
print(x)

# expandtabs
txt="k\te\tv\ti\tn"
x=txt.expandtabs(2)
print(x)

# find
txt="my name is kevin."
x=txt.find("kevin")
print(x)

# index
txt="my name is kevin."
x=txt.index("name")
print(x)

# isalnum
txt="my name is kevin12."
x=txt.isalnum()
print(x)

# isalpha
txt="my name is kevin."
x=txt.isalpha()
print(x)

# isascii
txt="my name is kevin."
x=txt.isascii()
print(x)

# isdecimal
txt="12354"
x=txt.isdecimal()
print(x)

# isdigit
txt="123456"
x=txt.isdigit()
print(x)

# isidentifier
txt="Kevin"
x=txt.isidentifier()
print(x)

# islower
txt="kevin"
x=txt.islower()
print(x)

# isnumeric
txt="3221"
x=txt.isnumeric()
print(x)

# isprintable
txt="hello is this #kevin."
x=txt.isprintable()
print(x)

# isspace
txt="  "
x=txt.isspace()
print(x)

# istitle
txt="Hello My Name Is Kevin."
x=txt.istitle()
print(x)

# isupper
txt="HELLO MY NAME IS KEVIN."
x=txt.isupper()
print(x)

# join()
Mytuple=("Smerah","kevin")
x=' '.join(Mytuple)
print(x)

# ljust
txt="hello"
x=txt.ljust(20)
print(x, "kevin.")

# lower
txt="hello my name is KEVIN."
x=txt.lower()
print(x)

# lstrip
txt="    kevin     "
x=txt.lstrip()
print("my name is",x)

# partition
txt="my name is kevin jose"
x=txt.partition("is")
print(x)

# replace
txt="my name is emmanual"
x=txt.replace("emmanual","kevin")
print(x)

# rsplit
txt="my name is kevin,jose"
x=txt.rsplit(",")
print(x)

# split
txt="my name is kevin"
x=txt.split()
print(x)


# splitlines
txt="thank you for coming\nwelcome to the jungle"
x=txt.splitlines()
print(x)

# startswith
txt="My name is kevin."
x=txt.startswith("My")
print(x)

# swapcase
txt="my name IS KEVIN."
x=txt.swapcase()
print(x)

# title
txt="my name is kevin."
x=txt.title()
print(x)

# upper
txt="my name is kevin."
x=txt.upper()
print(x)

# zfill
txt="100"
x=txt.zfill(50)
print(x)

