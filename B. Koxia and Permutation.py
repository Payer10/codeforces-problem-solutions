for i in range(int(input())):
    a,b=map(int,input().split())
    l=[]
    for i in range(a//2):
        l.append(a-i)
        l.append(i+1)
    if(a%2==1):
        l.append(a//2+1)
    print(*l)
   