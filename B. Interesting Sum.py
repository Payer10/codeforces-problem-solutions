for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    print(l[-1]-l[0] + l[-2]-l[1])