n=input()
m=input()
c=""
for i in range(len(n)):
    if((n[i]=="0" and m[i]=="1")or(n[i]=="1" and m[i]=="0")):
        c+="1"
    else:
        c+="0"
print(c)
