for i in range(int(input())):
    candy_Num=int(input())
    list_candy=list(map(int,input().split()))
    sum_list=sum(list_candy)
    if(sum_list%2==0 and sum_list//2 < candy_Num):
        print("YES")
    elif(candy_Num%2==0 and sum_list%2==0):
        print("YES")
    else:
        print("NO")
              
