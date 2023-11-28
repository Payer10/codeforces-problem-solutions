for i in range(int(input())):
    Number=int(input())
    list_Num=list(map(int,input().split()))
    even=0
    odd=0
    for j in range(len(list_Num)):
        if(list_Num[j]%2==0):
            even+=1
        else:
            odd+=1
    print(min(even,odd))
        
