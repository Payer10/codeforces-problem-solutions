for i in range(int(input())):
    number=int(input())
    lists=list(map(int,input().split()))
    sort=sorted(lists)
    for i in range(2,number):
        if(sort[i]==sort[i-2]):
            print(sort[i])
            break
    else:
        print('-1')
    
