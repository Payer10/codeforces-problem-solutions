for _ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())),reverse=True)
    for i in range(n//2):
        print(l[i],l[-1])