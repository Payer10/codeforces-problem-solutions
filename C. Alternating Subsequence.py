for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    a=s[0]
    count=0
    for i in range(n-1):
        if(s[i]*s[i+1])<0 :
            count+=a
            a=s[i+1]
        else:
            a=max(a,s[i+1])
    print(count+a)
   
