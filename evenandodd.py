# s="ads ss4  7ad3nf1 gfsg2 45gd675"
# ec=0
# oc=0
# os=''
# es=''

# for i in s:
#     if i.isnumeric():
#         i=int(i)
#         if i%2==0:
#             ec=ec+1
#             es=es+str(i)
#         else:
#             oc=oc+1
#             os=os+str(i)

# print(oc,ec)
# print(os,es)



# a="ads ss4  7ad3nf1 gfsg2 45gd675"
# oc=0
# for i in a:
#     if i.isnumeric():
#         i=int(i)
#         if i%2!=0:
#             oc=oc+i      
# print(oc)
# if oc%2==0:
#     print("sum of odd numbers is even")
# else:
#     print("sum of odd numbers is odd")



# a="ads ss4  7ad3nf1 gfsg2 45gd675" 
# for i in range(0,len(a)):
#     print(a[i],end="")


# i=0
# while i<len(a):
#     print(a[i],end="")
#     i=i+1


a=10
b=20
a,b=b,a
print(a,b)
