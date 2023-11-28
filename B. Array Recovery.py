for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    newli=[0]
    for j in range(n):
        if(l[j] != 0 and newli[-1]-l[j] >= 0):
           print(-1)
           break
        else:
            newli.append(newli[-1]+l[j])
    else:
        print(*newli[1:])
            
                
