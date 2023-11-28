def Following_direction(s,n):
    a,b=(0,0)
    for i in range(n):
        if(s[i]=='U'):
            a+=1
        if(s[i]=='D'):
            a-=1
        if(s[i]=='R'):
            b+=1
        if(s[i]=='L'):
            b-=1
        if(a,b)==(1,1):
            return('YES')
            break
    else:
        return('NO')
for _ in range(int(input())):
    n=int(input())
    s=input()
    print(Following_direction(s,n))


    
        
