def prime_number(m,n):
    prime=0
    for i in range(m,n+1):
        for j in range(2,int(i**.5)+1):
            if i%j==0:
                break
        else:
            prime+=1
    return prime
for i in range(int(input())):
    n,m=map(int,input().split())
    print(prime_number(n,m))