from math import ceil
for i in range(int(input())):
    a,b,c=map(int,input().split())
    n=abs(a-b)/2
    if n<c and n>0:
        print(1)
    else:
        print(ceil(n/c))
