for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in l:
        if i==k:
            print('YES')
            break
    else:
        print('NO')