for i in range(int(input())):
    w,h,n=map(int,input().split())
    m=w*h
    c=0
    while m%2==0:
        m=m//2
        c+=1
    if(2**c>=n):
        print('YES')
    else:
        print('NO')
