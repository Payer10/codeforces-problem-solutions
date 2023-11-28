for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum_a=sum(a)
    sum_b=sum(b)-max(b)
    print(sum_a+sum_b)
