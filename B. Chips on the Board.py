for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    min_a=min(a)
    min_b=min(b)
    ans1=0
    ans2=0
    for i in range(n):
        ans1+=(min_a+b[i])
        ans2+=(min_b+a[i])
    print(min(ans1,ans2))
