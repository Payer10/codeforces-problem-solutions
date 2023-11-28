for i in range(int(input())):
    Number=int(input())
    a=len(bin(Number)) - 3
    print(2**a - 1)
