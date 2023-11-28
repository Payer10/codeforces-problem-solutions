
for i in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    if(b>=0):
        print(a*n+b*n)
    else:
        print(n*a+b*(max(s.count('01'),s.count('10'))+1))

