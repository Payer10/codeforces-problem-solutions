for i in range(int(input())):
    s=input();n=len(s);p=0;l=-1
    for i in range(n-1,-1,-1):
        if int(s[i])+p > 4:
            p=1;l=i
        else:
            p=0
    if l>-1:
        if l==0:
            print('1'+'0'*n)
        else:
            print(s[:l-1]+str(int(s[l-1])+1)+'0'*(n-l))
    else:
        print(s)