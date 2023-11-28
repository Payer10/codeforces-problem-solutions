for i in range(int(input())):
    n,k=list(map(int,input().split()))
    s=input()
    st=set(s.lower())
    a=0
    b=0
    for i in st:
        a+=(s.lower().count(i)//2)
        b+=min(s.count(i),s.count(i.upper()))
    print(min(b+k,a))


