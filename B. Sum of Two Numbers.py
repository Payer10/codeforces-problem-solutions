def sum_two_Numbers(n):
    if n%2==0:
        return n//2,n//2
    if n%10!=9:
        return n//2,n//2 +1
    x,y=sum_two_Numbers(n//10)
    return 10*y+4,10*x+5
for i in range(int(input())):
    print(*sum_two_Numbers(int(input())))
