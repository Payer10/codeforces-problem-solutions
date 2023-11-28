for i in range(int(input())):
    a,b=map(int,input().split())
    s=input()
    idx=a
    t=''
    for j in range(a):
        if(int(s[j])<b):
            idx=j
            break
    t+=s[0:idx]
    t+=(str(b))
    t+=s[idx:a]
    print(t)
