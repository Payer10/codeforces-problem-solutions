for i in range(int(input())):
    Number=int(input())
    li=list(map(int,input().split()))
    for i in range(1,Number+1):
        if(i>=li[i-1]):
            print('YES')
            break
    else:
        print('NO')
