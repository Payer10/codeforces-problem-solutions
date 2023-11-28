for i in range(int(input())):
    num=int(input())
    li=list(map(int,input().split()))
    if(num==1):
        if(li[0]==1):
            print('Yes')
        else:
            print('No')
    else:
        for i in range(num-2):
            if(li[i]<=li[i-2]):
                print('Yes')
                break
        else:
            print('No')
                
