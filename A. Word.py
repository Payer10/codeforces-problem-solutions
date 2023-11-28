s=input()
l=len(s)
count=0
for i in s:
    if(i>="A" and i<="Z"):
        count+=1
if(count>(l/2)):
    print(s.upper())
else:
    print(s.lower())
       
