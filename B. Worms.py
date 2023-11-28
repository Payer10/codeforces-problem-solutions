N=int(input())
li_a=list(map(int,input().split()))
a=int(input())
li_b=list(map(int,input().split()))
for s in range(a):
    a1=li_b[s]
    count=0
    c=0
    for i in range(N):
        count+=li_a[i]
        c+=1
        if(count>=a1):
            break
    print(c)
