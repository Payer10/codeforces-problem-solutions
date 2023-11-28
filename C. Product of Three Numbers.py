import math
def solved(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            d = n // i
            for j in range(2, int(math.sqrt(d))+1):
                if d % j == 0:
                    return(i, j, d // j)
                    
    return None
        
for i in range(int(input())):
    Number=int(input())
    n=(solved(Number))
    if n:
        print('YES')
        print(n)
    else:
        print('NO')
                
