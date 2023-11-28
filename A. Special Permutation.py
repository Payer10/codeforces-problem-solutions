import itertools
for i in range(int(input())):
    Number=int(input())
    newlist=[]
    for i in range(1,Number+1):
        newlist.append(i)
    n=list(itertools.permutations(newlist))
    m=(Number-1)
    if(Number<5):
        print(*n[m**2])
    else:
        print(*n[Number**2+((Number*2)-2)])
