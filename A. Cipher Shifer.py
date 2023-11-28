for _ in range(int(input())):
    n=int(input())
    s=input()
    k=''
    j=''
    for i in s:
        if k=='':
            k=i
        elif k[0]==i:
            j+=k
            k=''
    print(j)
            

