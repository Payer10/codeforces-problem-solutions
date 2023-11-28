for _ in range(int(input())):
    s=input()
    l=''
    a='0'
    for i in range(len(s)):
        if s[i]=='?':
            l+=a
        else:
            a=s[i]
            l+=s[i]
    print(l)
