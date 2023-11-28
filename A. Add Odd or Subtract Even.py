for i in range(int(input())):
    ans=n=0
    a,b=map(int,input().split())
    if(a>b):
        n=a-b
        ans+=1
        if(n%2!=0):
            ans+=1
        print(ans)
    elif(a==b):
        print("0")
    else:
        n=b-a
        ans+=1
        if(n%2!=1):
            ans+=1
        print(ans)
