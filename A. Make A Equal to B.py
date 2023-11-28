def Make_A_Equal_To_B(n,a,b):
    num=0
    for i in range(n):
        if(a[i]!=b[i]):
            num+=1
    return(min(num,abs(sum(a)-sum(b))+1))

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(Make_A_Equal_To_B(n,a,b))
