for i in range(int(input())):
    num=int(input())
    list_a=list(map(int,input().split()))
    list_b=list(map(int,input().split()))
    frist=[]
    second=[]
    for i in range(num):
        max_a=max(list_a[i],list_b[i])
        frist.append(max_a)
        min_b=min(list_a[i],list_b[i])
        second.append(min_b)
    print(max(frist) * max(second))
        
