for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2==0:
        print(2,'\n',1,n,'\n',1,n)
    else:
        print(4,'\n',1,2,'\n',1,2,'\n',2,n,'\n',2,n)
