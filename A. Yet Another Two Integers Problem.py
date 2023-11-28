from math import ceil
for i in range(int(input())):
    frist_Number,second_Number=map(int,input().split())
    print(ceil(abs(frist_Number-second_Number)/10))
