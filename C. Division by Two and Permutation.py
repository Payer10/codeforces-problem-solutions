for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    new_list=set()
    for i in l:
        while (i in new_list or i>n) and i>1:
            #i>>=1
            i=i//2
        new_list.add(i)
    #print(['NO','YES'][len(new_list)==n])
    if(len(new_list)==n):
        print('YES')
    else:
        print('NO')
