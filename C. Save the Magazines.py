for _ in range(int(input())):
    n=int(input())
    s=input()
    l=list(map(int,input().split()))
    a=0
    b=0
    for i in range(n):
        if s[i]=='1':
            a+=max(l[i],b)
        if s[i]=='0' or l[i]<b:
            b=l[i]
    print(a)