for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(0)
    if(a<=(n+1)//2):
        print(0)
    elif(n==a or a+l.count(1)<n):
        print(1)
    else:
        print(2)