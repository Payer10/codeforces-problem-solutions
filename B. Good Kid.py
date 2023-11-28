for i in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    l[0]+=1
    a=1
    for i in l:
        a*=i
    print(a)