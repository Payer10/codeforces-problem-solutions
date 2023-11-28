for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li=[]
    lj=[]
    if(min(l)==max(l)):
        print(-1)
    else:
        for i in range(n):
            if l[i] == max(l):
                li.append(l[i])
            else:
                lj.append(l[i])
        print(len(lj),len(li))
        print(*lj)
        print(*li)
