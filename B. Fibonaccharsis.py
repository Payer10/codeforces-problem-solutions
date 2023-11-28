for i in range(int(input())):
    n,a=map(int,input().split())
    if a-n > 2:
        print(0)
        continue
    elif a==1:
        print(1)
    for i in range(2,a):
        if n%i==0 and a%i==0:
            print(i)
            break
