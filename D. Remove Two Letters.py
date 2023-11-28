for i in range(int(input())):
    n=int(input())
    s=input()
    c=n-1
    for i in range(1,n-1):
        if s[i-1]==s[i+1]:
            c-=1
    print(c)