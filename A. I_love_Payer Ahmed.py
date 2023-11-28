Number=int(input())
listdigit=list(map(int,input().split()))
counter=0
for i in range(1,Number):
    highest_count=0
    lowest_count=0
    for a in range(0,i):
        if(listdigit[i]>listdigit[a]):
            highest_count+=1
        elif(listdigit[i]<listdigit[a]):
            lowest_count+=1
    if(highest_count==i or lowest_count==i):
        counter+=1
print(counter)

