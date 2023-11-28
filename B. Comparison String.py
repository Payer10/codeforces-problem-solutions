for _ in range(int(input())):
    n=int(input())
    s=input()
    a=1
    b=1
    for i in range(1,n):
        if(s[i]==s[i-1]):
            a+=1
        else:
            b=max(a,b)
            a=1
    b=max(b,a)
    print(b+1)
