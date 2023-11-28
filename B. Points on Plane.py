for i in range(int(input())):
    Number=int(input())
    n=int(Number**.5)
    if(n*n>=Number):
        print(n-1)
    else:        
        print(n)
