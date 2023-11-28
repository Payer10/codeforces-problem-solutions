for i in range(int(input())):
    n=int(input())
    s=input()
    ans=n
    for i in range(1,n):
        if s[i]!=s[i-1]:
            ans+=i
    print(ans)