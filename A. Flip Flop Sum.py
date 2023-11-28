for i in range(int(input())):
    n=int(input())
    s=input()
    l=list(map(int,s.split()))
    if '-1 -1' in s:
        print(sum(l)+4)
    elif '-1' in s:
        print(sum(l))
    else:
        print(sum(l)-4)
        