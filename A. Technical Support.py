for _ in range(int(input())):
    n=int(input())
    s=input()
    q=0
    for i in s:
        if(i=='Q'):
            q+=1
        elif(i=='A'):
            q=max(q-1,0)
    if(q>0):
        print('No')
    else:
        print('Yes')
