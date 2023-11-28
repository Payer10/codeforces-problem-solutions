def divisor(n):
    for i in range(2,int(n**.5)+1):
        if(n%i==0):
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    a=n+1
    while not divisor(a):
        a+=1
    b=a+n
    while not divisor(b):
        b+=1
    print(a*b)