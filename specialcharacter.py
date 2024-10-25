a="my name is kevin #$"
spc=0
for i in a:
    if (i.isalnum()==False) and (i.isspace()==False):
        spc=spc+1
        
print(spc)