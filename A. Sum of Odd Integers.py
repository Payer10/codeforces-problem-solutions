for i in range(int(input())):
    a,b=map(int,input().split())
    odd=[]
    count=0
    for j in range(1,a+1):
        if(j%2==1):
            odd.append(j)
    if(a in odd):
        print('YES')
    elif(sum(odd)==a):
        print('YES')
    else:
        for i in range(len(odd)):
            if(odd[i]<=a or a in odd):
                a=a-odd[i]
                count+=1
                if(count==b):
                    break
        if(a==0):
            print('YES')
        else:
            print('NO')
        
