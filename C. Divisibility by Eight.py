n=input()
if(max(n)==min(n)):
    print('NO')
else:
    for i in n:
        a=n.replace(i, '')
        if(int(a)%8==0):
            print('YES')
            print(a)
            break
    else:
        print('NO')
