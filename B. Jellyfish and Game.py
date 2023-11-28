for i in range(int(input())):
    a,b,n=map(int,input().split())
    la=sorted(map(int,input().split()))
    lb=sorted(map(int,input().split()))
    if la[0]<lb[-1]:
        la[0],lb[-1]=lb[-1],la[0]
    if n%2==1:
        print(sum(la))
    else:
        print(sum(la)-max(la)+min(lb))