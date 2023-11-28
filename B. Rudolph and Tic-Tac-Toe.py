for i in range(int(input())):
    a=input()
    b=input()
    c=input()
    ans='.'
    if (a[0]==b[0]==c[0] or a[0]==a[1]==a[2]) and ans=='.':
        ans=a[0]
    if (a[1]==b[1]==c[1] or b[0]==b[1]==b[2] or a[0]==b[1]==c[2] or a[2]==b[1]==c[0]) and ans=='.':
        ans=b[1]
    if (a[2]==b[2]==c[2] or c[0]==c[1]==c[2]) and ans=='.':
        ans=c[2]
    if ans == '.':
        print('DRAW')
    else:
        print(ans)

