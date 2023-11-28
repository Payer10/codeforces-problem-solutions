for i in range(int(input())):
    s=input()
    newli=[]
    for j in range(len(s)):
        newli.append(s[j])
    if("A" in newli and "B" in newli):
        newli.remove('A')
        newli.remove('B')
        a=newli.count("A")
        b=newli.count("B")
        if(a==b):
            print("YES")
        else:
            print("NO")
        
    else:
        if("B" in newli and 'C' in newli):
            newli.remove('B')
            newli.remove('C')
            b=newli.count("B")
            c=newli.count("C")
            if(b==c):
                print("YES")
            else:
                print("NO")
                         
        
        
