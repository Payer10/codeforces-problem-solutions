for _ in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    for i in range(1,n):
        a=s[i]+s[i-1]
        if a not in l:
            l.append(a)
    print(len(l))
        
        
