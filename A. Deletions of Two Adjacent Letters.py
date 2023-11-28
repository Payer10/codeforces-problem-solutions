for i in range(int(input())):
    s=input()
    a=input()
    li=[]
    if(s[0]==a):
        print('YES')
    else:
        for i in range(2,len(s)):
            if(s[i]==a):
                print('YES')
                break
        else:
            print('NO')
