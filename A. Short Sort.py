for i in range(int(input())):
    s='abc'
    a=input()
    c=0
    for i in range(3):
        if s[i]!=a[i]:
            c+=1
    if c<3:
        print('YES')
    else:
        print('NO')