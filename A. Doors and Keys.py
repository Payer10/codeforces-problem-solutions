for i in range(int(input())):
    s=input()
    for i in range(1,len(s)):
        if (s[i]=="B" and s[i-1]=="b") and (s[i]=="R" and s[i-1]=="r") and (s[i]=="G" and s[i-1]=="g") :
            print('YES')
            break
    else:
        print('NO')