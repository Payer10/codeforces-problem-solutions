for _ in range(int(input())):
    n=int(input())
    a=n//2+n%2
    print(a)
    l=1
    r=3*n
    while l<r:
        print(l,r)
        l+=3
        r-=3
