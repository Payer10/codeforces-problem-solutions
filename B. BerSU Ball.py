n=int(input())
listn=list(map(int,input().split()))
m=int(input())
listm=list(map(int,input().split()))
nNum=sorted(listn)
mNum=sorted(listm)
count=0
b=min(n,m)
for i in range(b):
    if(abs(mNum[i] - nNum[i]) <= 1):
        count+=1
    else:
        if(n>m):
            a=m
            u=n-m
            for j in range(u):
                if(abs(nNum[a] - mNum[m-1]) <= 1):
                    a+=1
                    count+=1
                if(a==n):
                    break       
        if(m>n):
            l=n
            o=m-n
            for h in range(o):
                if(abs(nNum[n-1] - mNum[l]) <= 1):
                    l+=1
                    count+=1
                if(l==m):
                    break
print(count)
            
