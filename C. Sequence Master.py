for i in range(int(input())):
    Num=int(input())
    Numli=list(map(int,input().split()))
    count=0
    for j in range(len(Numli)):
        if(Numli[j]<=0):
            count+=abs(Numli[j])
        else:
            count+=(max(Numli)-Numli[j])
    if(min(Numli)<0):
        print(count+1)
    else:
        print(count)
