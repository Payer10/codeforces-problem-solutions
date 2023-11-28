import math
for i in range(int(input())):
    a=int(input())
    li=list(map(int,input().split()))
    n=0
    for i in range(a//2):
        n1=li[i]
        n2=li[a-i-1]
        n=math.gcd(n,abs(n1-n2))
    print(n)
