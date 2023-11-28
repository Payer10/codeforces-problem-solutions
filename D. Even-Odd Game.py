for _ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())),reverse=True)
    a=0
    for i in range(n):
        if(i%2==0):
            if(l[i]%2==0):
                a+=l[i]
        else:
            if(l[i]%2==1):
                a-=l[i]
    if a==0:
        print('Tie')
    elif a>0:
        print('Alice')
    else:
        print('Bob')
            
        
        
