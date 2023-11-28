for _ in range(int(input())):
    n=int(input())
    nl=list(map(int,input().split()))
    m=int(input())
    ml=list(map(int,input().split()))
    a=0
    b=0
    for i in nl:
        a+=i
        b=max(a,b)
    a=b  
    for j in ml:
        a+=j
        b=max(a,b)
    print(b)
