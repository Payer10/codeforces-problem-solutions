for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(min(l)<0):
        print(min(l))
    else:
        print(max(l))
