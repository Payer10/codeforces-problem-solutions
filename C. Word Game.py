for i in range(int(input())):
    n=int(input())
    a=set(input().split())
    b=set(input().split())
    c=set(input().split())
    x=3*len(a-b-c) + len(a&b-c) + len(a&c-b)
    y=3*len(b-a-c) + len(b&c-a) + len(b&a-c)
    z=3*len(c-b-a) + len(c&a-b) + len(c&b-a)
    print(x,y,z)
        
