from math import*
def prime(Number):
    count=0
    for i in range(1,Number+1):
        if(Number%i==0):
            count+=1
    if count==3:
        return "YES"
    return "NO"
fristNumber=int(input())
listNumber=list(map(int,input().split()))
for i in range(fristNumber):
    print(prime(listNumber[i]))
    
