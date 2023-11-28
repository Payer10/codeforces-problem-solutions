for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    c=0
    for i in range(n//2):
        c+=abs(l[i]-l[n-i-1])
    print(c)