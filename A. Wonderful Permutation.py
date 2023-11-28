for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    n=sorted(l)
    c=0
    for i in range(1,b+1):
        if(a==1 or l[i]==n[i]):
            c=0
            break
        else:
            c+=1
    print(c)
