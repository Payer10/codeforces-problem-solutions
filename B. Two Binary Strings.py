for i in range(int(input())):
    a=input()
    b=input()
    for i in range(1,len(a)):
        if a[i-1]==b[i-1]=='0' and a[i]==b[i]=='1':
            print('YES')
            break
    else:
        print('NO')

