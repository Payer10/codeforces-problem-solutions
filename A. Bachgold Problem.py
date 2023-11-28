Number=int(input())
if(Number%2==0):
    n=Number//2
    a=(list(str(2)*n))
    print(n)
    print(*a)
else:
    n=(Number//2)-1
    li=list(str(2))*n
    a=li
    b=2+1
    print(n+1)
    print(*a,b)
    
