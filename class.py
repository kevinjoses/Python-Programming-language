# # Q1
# class car():
#     def __init__(self):
#         self.year=2018
#         self.type="automatic"
#         self.engine="petrol"

#     def details(self,a,b,c):
#         print("model",a)
#         print("brand",b)
#         print("year",c)


# obj=car()
# obj.details("m4","bmw",2018)

# Q2

# class car():
#     def __init__(self,a,b,c):
#         self.year=a
#         self.type=b
#         self.engine=c

#     def display(self):
#         print(self.year,self.type,self.engine)
        


# w=car(2018,"auto","petrol")
# w.display()

# q=car(2024,"auto","diesel")
# q.display()


class car():
    def read(self,b,m,y):
        self.year=y
        self.brand=b
        self.model=m
    
    def display(self):
        print(self.brand)
        print(self.year)
        print(self.model)

c=car()
brand=input("enter brand:")
model=input("enter model name:")
year=2019
c.read(m=model,b=brand,y=year)
c.display()