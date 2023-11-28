for i in range(int(input())):
    Number=int(input())
    even=[]
    odd=[]
    a=Number//2
    if(a%2==1):
        print('NO')
    else:
        for j in range(1,Number+1):
            if(j%2==0):
                even.append(j)
            else:
                odd.append(j)
        b=sum(even) - sum(odd)
        odd[len(odd)-1]=odd[len(odd)-1]+b
        even.extend(odd)
        print('YES')
        print(*even)
        
