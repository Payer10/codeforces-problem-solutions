for i in range(int(input())):
    Num=int(input())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    min1=min(li1)
    min2=min(li2)
    ans=0
    for a in range(Num):
        ans+=max(li1[a]-min1,li2[a]-min2)
    print(ans)
