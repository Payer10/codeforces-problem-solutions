for i in range(int(input())):
    a,b=map(int,input().split())
    ali=list(map(int,input().split()))
    bli=list(map(int,input().split()))
    count=-2
    for i in range(a):
        if((ali[i]+i)<=b and (count==-2 or bli[count]<bli[i])):
            count=i
    print(count+1)
            
