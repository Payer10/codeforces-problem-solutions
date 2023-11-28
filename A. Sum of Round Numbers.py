for i in range(int(input())):
    Number=input()
    li=[]
    for a in range(len(Number)):
        if(Number[a]!='0'):
            b=Number[a] + '0'*(len(Number)-a-1)
            li.append(b)
    print(len(li))
    print(*li)
