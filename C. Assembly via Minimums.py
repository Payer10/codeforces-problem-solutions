for i in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    s=0
    for i in range(n-1,0,-1):
        print(l[s],end=' ')
        s+=i
    print(l[-1])