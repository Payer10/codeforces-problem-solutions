for i in range(int(input())):
    Number=int(input())
    temp=Number & (Number-1)
    if(temp==0):
        print("NO")
    else:
        print("YES")
