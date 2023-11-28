for i in range(int(input())):
    n,k=map(int,input().split())
    s=input().strip()
    a=0
    k-=1
    i=0
    while i<n:
        if s[i]=='B':
            a+=1
            i+=k
        i+=1
    print(a)