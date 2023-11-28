for i in range(int(input())):
    n,a,q=map(int,input().split())
    s=input()
    num=a
    p=a
    for i in s:
        if i=='+':
            a+=1
            p+=1
            num=max(num,a)
        else:
            a-=1
    if num>=n:
        print('YES')
    elif p<n:
        print('NO')
    else:
        print('MAYBE')
