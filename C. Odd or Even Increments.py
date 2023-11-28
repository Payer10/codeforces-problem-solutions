for i in range(int(input())):
    num=int(input())
    li=list(map(int,input().split()))
    for i in range(num-2):
        if(li[i]%2!=li[i+2]%2):
            print('NO')
            break
    else:
        print('YES')
