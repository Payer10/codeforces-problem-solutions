for i in range(int(input())):
    n=int(input())
    s=input()
    a=set(s[0::2])
    b=set(s[1::2])
    if a & b :
        print('NO')
    else:
        print('YES')
