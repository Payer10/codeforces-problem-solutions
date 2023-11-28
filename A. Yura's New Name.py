for i in range(int(input())):
    s=input()
    count=0
    for a in range(len(s)-1):
        if(s[a]=='_' and s[a+1]=='_'):
            count+=1
    print(count)
            
