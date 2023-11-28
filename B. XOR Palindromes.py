for _ in range(int(input())):
    n=int(input())
    s=input()
    b=[0]*(n+1)
    x=n//2
    z=0
    for i in range(0,x):
        if s[i]!=s[n-i-1]:
            z+=1
    for i in range(x-z+1):
        b[z]=1
        b[z+n%2]=1
        z+=2
    print(*b, sep='')