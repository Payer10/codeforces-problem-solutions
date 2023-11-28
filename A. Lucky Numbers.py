for i in range(int(input())):
    a,b=map(int,input().split())
    newli=0
    nli=a
    for j in range(a,b+1):
        s=str(j)
        n=int(max(s))-int(min(s))
        if(newli<=n):
            nli=j
            newli=n
            if(newli==9):
                break
    print(nli)
        
