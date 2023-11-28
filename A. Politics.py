for _ in range(int(input())):
    a,b=map(int,input().split())
    count=0
    c=0
    for _ in range(a):
        s=input()
       # x=s.replace('+', '1').replace('-', '0')
        #if(min(x)=='1'):
        if('-' in s):
            count+=1
        else:
            c+=1
    j=a-max(count,c)
    if(j==0):
        print(j+1)
    else:
        print(j)
