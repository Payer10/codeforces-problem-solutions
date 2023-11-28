for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    even,odd=[],[]
    for i in range(n):
        if(l[i]%2==0):
            even.append(i+1)
        else:
            odd.append(i+1)
    if(len(odd)>=1 and len(even)>=2):
        print('YES')
        print(odd[0],even[0],even[1])
    elif(len(odd)>=3):
        print('YES')
        print(odd[0],odd[1],odd[2])
    else:
        print('NO')
