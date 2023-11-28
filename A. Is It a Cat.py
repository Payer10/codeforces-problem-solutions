for i in range(int(input())):
    N=int(input())
    s=input().lower()
    li=''
    li+=s[0]
    for i in range(1,N):
        if(s[i]!=s[i-1]):
            li+=s[i]
    if(li=='meow'):
        print('YES')
    else:
        print('NO')
