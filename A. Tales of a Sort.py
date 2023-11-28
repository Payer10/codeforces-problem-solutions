for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    max_item=0
    for i in range(n):
        if(l[i]!=s[i]):
            max_item=max(max_item,s[i],l[i])
    print(max_item)