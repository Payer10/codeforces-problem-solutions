n,k=map(int,input().split())
l=sorted(map(int,input().split()))
count=0
if(n==1):
    print(1)
else:
    for i in l:
        if(min(l)<i):
            count+=1
    print(count)
