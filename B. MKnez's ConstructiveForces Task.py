for i in range(int(input())):
    n=int(input())
    if(n%2==1 and n<5):
        print('NO')
    else:
        l=[]
        for i in range(1,n+1):
            if(n%2==0):
                if(i%2==0):
                    l.append(-1)
                else:
                    l.append(1)
            else:
                if(i%2==1):
                    l.append((n//2) -1)
                else:
                    l.append(-(n//2))
        print('YES')
        print(*l)
