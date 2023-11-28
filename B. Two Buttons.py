n,m=map(int,input().split())
w=0
while (n!=m):
    if(m>n):
        if(m%2==0):
            m/=2
            w+=1
        else:
            m+=1
            w+=1
    else:
        m+=1
        w+=1
print(w)
