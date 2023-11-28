for i in range(int(input())):
    a,b=map(int,input().split())
    l=[]
    for i in range(a):
        l.append(min((1+(i*(i+1)//2),(b-a+i+1))))
    print(*l)
