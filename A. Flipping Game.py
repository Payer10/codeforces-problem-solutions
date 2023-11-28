Number=int(input())
frist_list=list(map(int,input().split()))
print(sum(frist_list))
if(sum(frist_list)==0):
    print(Number)
elif(sum(frist_list)==Number):
    print(Number-1)
else:
    count=0
    for i in range(len(frist_list)-1):
        count+=frist_list[i]
    if(count==2):
        print(Number-1)
    else:
        print(Number)

