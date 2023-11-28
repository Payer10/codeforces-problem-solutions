for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=sorted(l)
    if(a==l):
        print(0)
    elif(l[0]==1 or l[n-1]==n):
        print(1)
    elif(l[0]==n and l[n-1]==1):
        print(3)
    else:
        print(2)
