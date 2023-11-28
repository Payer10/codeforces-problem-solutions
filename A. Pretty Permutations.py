for i in range(int(input())):
    Number=int(input())
    even=[]
    odd=[]
    for a in range(Number):
        if((Number-a)%2==0):
            even.append(Number-a)
        else:
            odd.append(Number-a)
    even.extend(odd)
    print(*even)
