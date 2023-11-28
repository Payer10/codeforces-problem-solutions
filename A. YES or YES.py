for i in range(int(input())):
    s=input()
    if(len(s)==1):
        if(s[0]=='Y' or s[0]=='e' or s[0]=='s'):
            print('YES')
        else:
            print('NO')
    for j in range(len(s)):
        if(i+1 == len(s)):
            break
        if(s[i]=='e' and s[i+1]=='s'):
            continue
        elif(s[i]=='Y' and s[i+1]=='e'):
            continue
        elif(s[i]=='s' and s[i+1]=='Y'):
            continue
        else:
            print('NO')
            break
    print('YES')
