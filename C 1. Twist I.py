for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=[0]*102
    for i in l:
        m[i+1]=max(m[i+1],m[i]+1)
        m[i]=max(m[i],m[i-1]+1)
    print(max(m))