for i in range(int(input())):
    s=input()
    ans=10**s.count('?')
    if(s[0]=='0'):
        ans=0
    elif(s[0]=='?'):
        ans*=0.9
    print(int(ans))
