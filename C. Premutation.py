for _ in range(int(input())):
    li=[]
    for _ in range(int(input())):
        l=list(map(int,input().split()))
        li.append(l)
    li.sort()
    if li[0][0] == li[1][0]:
        print(li[0][0],*li[-1])
    else:
        print(li[1][0],*li[0])
