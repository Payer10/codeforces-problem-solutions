a=input()
b=sorted(list(a))
c=0
for i in range(len(b)):
    if(b[i]!="{" and b[i]!="}" and b[i]!="," and b[i]!=" "):
        if(b[i]!=b[i-1]):
            c+=1
print(c)
