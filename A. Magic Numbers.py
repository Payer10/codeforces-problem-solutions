n=input()
c=0
m=0
d=0
if(n[0]!='1' or '444' in n or '2' in n or '3' in n or '5' in n or '6' in n or'7' in n or '8' in n or '9' in n or '0' in n):
    print('NO')
else:
    for i in range(len(n)):
        m+=int(n[i])
        if((i+1)==len(n)):
            break
        if(n[i]=='1' and n[i+1]=='4'):
            c+=1
        else:
            c+=0
    if(len(n)==m or c>=1):
        print('YES')
    else:
        print('NO')

        
