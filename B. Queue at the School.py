t,n=map(int,input().split())
l=input()
b=t/n
if(b%2==1):
    print(*tuple(reversed(l)))
else:
    print(l)
