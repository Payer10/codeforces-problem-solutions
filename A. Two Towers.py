for i in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    b=input()
    a=a+b[::-1]
    s=0
    for i in range(n+m-1):
        if(a[i]==a[i+1]):
            s+=1
    if(s<2):
        print('Yes')
    else:
        print('No')
            




                
