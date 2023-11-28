for i in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    if(l[0]!=1):
        print('NO')
    else:
        ans=1
        for i in l[1:]:
            if i>ans:
                print('NO')
                break
            ans+=i
        else:
            print('YES')
            