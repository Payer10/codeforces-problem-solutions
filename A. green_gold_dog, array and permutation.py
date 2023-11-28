for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    for i in range(n):
        s.append([l[i],i])
    s.sort()
    l2=[0]*n
    c=0
    for i in s:
        l2[i[1]]=n-c
        c+=1
    print(*l2)
    
        
