for _ in range(int(input())):
    s=input()
    p=int(input())
    a=[ord(x)-ord('a')+1 for x in s]
    m=sum(a)
    b=sorted([(x,i)for i,x in enumerate(a)])
    while m>p:
        m-=b.pop()[0]
    c=sorted([(i,x) for x,i in b])
    print(''.join([chr(x+ord('a')-1)for i,x in c]))
