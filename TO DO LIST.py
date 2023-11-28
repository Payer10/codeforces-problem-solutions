for i in range(int(input())):
    Number=int(input())
    li=sorted(map(int,input().split()))
    count=0
    for a in range(Number):
        if(li[a]>=1000):
            count+=1
    print(count)
