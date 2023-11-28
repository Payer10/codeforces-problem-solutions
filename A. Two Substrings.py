string=input()
a=string.find('AB')
b=string.find('BA',a+2)
c=string.find('BA')
d=string.find('AB',c+2)
if((a!=-1 and b!=-1) or (c!=-1 and d!=-1)):
    print('YES')
else:
    print('NO')
