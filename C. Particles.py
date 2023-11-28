for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    even=0
    odd=0
    for i in range(n):
        if i%2==0:
            even+=max(l[i],0)
        else:
            odd+=max(l[i],0)
    a=(max(even,odd))
    if(a==0):
        print(max(l))
    else:
        print(a)