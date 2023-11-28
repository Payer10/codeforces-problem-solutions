for i in range(int(input())):
    a,b=map(int,input().split())
    print(min(a+1,2**min(b,30)))