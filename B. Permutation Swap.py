for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=sorted(l)
    s=n//2
    b=a[s]
    #print(b)
    c=0
    j=s
    for i in range(n//2):
        if(l[j]<=b):
            c+=1
            j+=1
    d=0
    k=s
    for i in range(n//2):
        if(l[k]>=b):
            d+=1
            k-=1
    print(max(c,d))




            
        
