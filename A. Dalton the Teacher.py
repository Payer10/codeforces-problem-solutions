from math import ceil
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(i+1==l[i]):
            c+=1
    print(ceil(c/2))
    