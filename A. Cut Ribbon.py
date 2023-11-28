while True:
    n,a,b,c=map(int,input().split())
    s1=(a,b,c)
    s=sorted(s1)
    a1=n//a
    b1=n//b
    c1=n//c
    a2=a1*a
    b2=b1*b
    c2=c1*c
    a3=n-a2
    b3=n-b2
    c3=n-c2
    if(a==n and b==n and c==n):
        print('1')
        break
    if(a3%b==0 and a3>0):
        print((a3//b)+a1)
        break
    elif(a3%c==0 and a3>0):
        print((a3//c)+a1)
        break
    elif((n-(s[0]+s[1]))%s[0]==0 and n%2==1):
        print(2+(n-(s[0]+s[1]))//s[0])
        break
    elif(b3%a==0 and b3>0):
        print((b3//a)+b1)
        break
    elif(b3%c==0 and b3>0):
        print((b3//c)+b1)
        break
    elif(c3%a==0 and c3>0):
        print((c3//a)+c1)
        break
    elif(c3%b==0 and c3>0):
        print((c3//b)+c1)
        break

