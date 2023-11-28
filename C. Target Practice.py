for i in range(int(input())):
    x=0
    for j in range(10):
        s=input()
        for k in range(10):
            if s[k]=='X':
                a=min(k,9-k,9-j,j)
                x+=a+1
    print(x)
