for i in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    newNum=sum(li)
    if(((newNum) - N)>=0):
        print((newNum) - N)
    else:
        print(1)
        
