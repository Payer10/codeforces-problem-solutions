for i in range(int(input())):
    s=input()
    one=0
    zero=0
    for i in range(len(s)):
        if(s[i]=="1"):
            one+=1
        else:
            zero+=1
    turn=min(one,zero)
    if(turn%2==0):
        print("NET")
    else:
        print("DA")
