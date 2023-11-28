for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    if(li[0]==1):
        li[0]=2
    for i in range(1,n):
        if(li[i]==1):
            li[i]+=1
        if(li[i]%li[i-1]==0):
            li[i]+=1
    print(*li)
        
