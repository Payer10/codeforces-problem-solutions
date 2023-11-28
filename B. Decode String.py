for _ in range(int(input())):
    n=int(input())
    s=input()
    string=' abcdefghijklmnopqrstuvwxyz'
    v=''
    for i in range(n-1):
        sub_str=int(s[i]+s[i+1])
        if(s[0]=='3' or s[0]=='2'):
            if(sub_str<=26):
                v+=string[sub_str]
                continue
            else:
                v+=string[int(s[i])]
        else:
            v+=string[int(s[i])]
    print(v)
        
