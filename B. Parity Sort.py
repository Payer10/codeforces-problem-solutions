for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    for i in range(n):
        if(s[i]%2!=l[i]%2):
            print('NO')
            break
    else:
        print('YES')