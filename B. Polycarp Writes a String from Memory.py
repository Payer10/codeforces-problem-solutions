for _ in range(int(input())):
    l=[]
    d=1
    for i in input():
        if(i not in l):
            l.append(i)
        if(len(l)>3):
            l=[i]
            d+=1
    print(d)            
