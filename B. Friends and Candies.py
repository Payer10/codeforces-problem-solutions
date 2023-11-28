for i in range(int(input())):
    Number=int(input())
    li=sorted(map(int,input().split()))
    if(Number==1):
        print(0)
    else:
        if(sum(li)%Number!=0):
            print(-1)
        else:
            count=0
            b=sum(li)//Number
            for a in li:
                if(b<a):
                    count+=1
            print(count)
        
