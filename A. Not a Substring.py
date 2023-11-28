for i in range(int(input())):
    s=input()
    n=len(s)
    if '((' in s or '))' in s:
        print('YES')
        print('()'*n)
    elif ')(' in s:
        print('YES')
        print('('*n+')'*n)
    else:
        print('NO')