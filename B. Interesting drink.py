import bisect
fristNum=int(input())
listdigit=sorted(map(int,input().split()))
for i in range(int(input())):
    Number=int(input())
    print(bisect.bisect(listdigit,Number))
    
