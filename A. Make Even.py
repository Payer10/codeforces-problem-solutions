for i in range(int(input())):
    Number=int(input())
    c=0
    if(Number<20):
        if(Number%2==0):
            print('0')
        else:
            print('-1')
    else:
        if(Number%2==0):
            print('0')
        else:
            s=str(Number)
            for i in range(len(s)):
                if(int(s[i])%2==1):
                    c+=1
            if(c==len(s)):
                print('-1')
            else:
                print(c)
