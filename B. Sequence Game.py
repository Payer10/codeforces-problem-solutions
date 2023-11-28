for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li=[l[0]]
    for i in range(1,n):
        if l[i]<l[i-1]:
            li.append(l[i])
        li.append(l[i])
    print(len(li))
    print(*li)