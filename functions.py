
# calling a function

def my_function():
  print("Hello from a function")

my_function()

# arguments in function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# passing a list as an argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(x,y,z):
  if x>y and x>z:
    return x
  elif y>x and y>z:
    return y
  else:
    return z
print(my_function(3,6,2))
    
  
