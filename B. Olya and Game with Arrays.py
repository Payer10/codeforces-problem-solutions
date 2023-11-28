for i in range(int(input())):
    minl=1000000000
    midl=[]
    for i in range(int(input())):
        n=int(input())
        l=sorted(map(int,input().split()))
        minl=min(minl,l[0])
        midl.append(l[1])
    print(sum(midl)-min(midl)+minl)
