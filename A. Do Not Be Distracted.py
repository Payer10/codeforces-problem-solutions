for i in range(int(input())):
    Number=int(input())
    s=input()
    for i in range(len(s)):
        if(s[i] in s[:i] and  s[i]!=s[i-1]):
            print('NO')
            break
    else:
        print('YES')
    
    
