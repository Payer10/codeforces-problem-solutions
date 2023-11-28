for i in range(int(input())):
    Number=int(input())
    liNum=list(map(int,input().split()))
    print(max(liNum) - min(liNum))
