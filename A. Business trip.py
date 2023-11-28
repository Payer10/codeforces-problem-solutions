k=int(input())
month=list(map(int,input().split()))
if(k==0):
    print('0')
elif(sum(month)<k):
    print('-1')
else:
    sort_month=sorted(month)
    new_month=list(reversed(sort_month))
    count=0
    sumNum=0
    for i in range(len(month)):
        count+=new_month[i]
        sumNum+=1
        if(count>=k):
            break
    print(sumNum)
