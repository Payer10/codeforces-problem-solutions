for i in range(int(input())):
    Number=int(input())
    li=list(map(int,input().split()))
    sortedli=sorted(li)
    sumn=0
    num=0
    for i in range(0,Number-1):
        if(abs(sortedli[i]-sortedli[i+1])==1):
            sumn+=1
    for i in range(Number):
        if(sortedli[i]%2==0):
            num+=1
    if(sumn>0 or num%2==0):
        print('YES')
    else:
        print('NO')
