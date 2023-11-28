def Teleportes(a,b,s):
    c=0
    sumb=0
    for i in range(a):
        if(s[i]<b):
            sumb+=s[i]
            if(sumb>b):
                break
            else:
                c+=1
    if(c<3):
        if(c==0):
            return 0
        else:
            return 1
    else:
        return 2
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=sorted(map(int,input().split()))
    print(Teleportes(a,b,s))





