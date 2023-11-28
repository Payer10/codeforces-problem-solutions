a=input()
c=a[0]
b=(a[1:])
if(a==a.upper()):
    print(a.lower())
elif(a==a.lower() and len(a)>1):
    print(a)
elif(len(a)==1 and a==a.lower()):
    print(a.upper())
elif(len(a)==4 and a[0]==a[0].lower()):
    print(c.upper()+b.lower())
else:
    print(a)
 
