Number=int(input())
newli=[]
if(Number%2==1):
    print(-1)
else:
    for i in range(1,Number+1):
        if(i%2==1):
            i=i+1
            newli.append(i)
        else:
            i=i-1
            newli.append(i)
    print(*newli)
