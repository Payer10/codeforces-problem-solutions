for i in range(int(input())):
    a=int(input())
    new=[]
    n=0
    for j in range(1,a+1):
        new.append(j)
    for h in range(0,a-1):
        n=max(new)-min(new)
        new.remove(max(new))
        new.remove(min(new))
        new.append(n)
    print(n)
    #print(*new)
