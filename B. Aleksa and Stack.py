for i in range(int(input())):
    n=int(input())
    ans=1
    l=[1]
    for i in range(n-1):
        ans+=2
        l.append(ans)
    print(*l)