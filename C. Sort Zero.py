for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    b=set()
    k=0
    for i in range(1,n):
        if(l[i]<l[i-1] or l[i] in b):
            for j in l[k:i]:
                b.add(j)
            k=i
    print(len(b))