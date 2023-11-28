s=input()
newli=''
for i in s:
    if(i=='Q'):
        newli+=(i)
    if(i=='A'):
        newli+=(i)
a=newli.replace('QAQ','2')
b=newli.replace('AQ','1')
c=newli.replace('Q','0')
print(newli)
print(int(a)+int(b)+int(c))
    
