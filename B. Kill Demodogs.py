l=10**9 +7
for i in range(int(input())):
    n=int(input())
    m=(n*(n+1)*(4*n-1))//6
    print(2022*m%l)
    