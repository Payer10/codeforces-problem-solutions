for i in range(int(input())):
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    odd=0
    even=0
    a1=0
    a2=0
    if(a==1):
        if(s[0]%2==0):
            print('NO')
        else:
            print('YES')
    else:
        for j in range(len(s)):
            if(s[j]%2==1):
                odd+=1
            else:
                even+=1
        if(odd==b):
            a1=odd
        elif(odd>b):
            a1=b
        else:
            if(b>=even and odd>=even):
                a1=odd+(2*(b-odd))
            if(odd<even):
                a2=even+(b-even)
        if(a1%2==1 or a2%2==1):
            print('YES')
        else:
            print('NO')
            
            
            
