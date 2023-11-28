for i in range(int(input())):
    Number=int(input())
    Number_list=list(map(int,input().split()))
    sorted_list=sorted(Number_list)
    count=0
    if(Number==1):
        print('YES')
    else:
        for i in range(len(sorted_list)):
            if((i+1)==Number):
                break
            if((abs(sorted_list[i]-sorted_list[i+1]))<=1):
                count+=1
        if(count==Number-1):
            print('YES')
        else:
            print('NO')
                
