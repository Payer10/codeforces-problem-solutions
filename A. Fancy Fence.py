for i in range(int(input())):
    Number=int(input())
    if(360 % (180 - Number) == 0):
        print("YES")
    else:
        print("NO")
