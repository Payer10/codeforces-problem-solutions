for i in range(int(input())):
    n=int(input())
    sum=n
    while n!=0:
        n=n//2
        sum+=n
    print(sum)
