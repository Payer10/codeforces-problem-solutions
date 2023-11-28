Number=list(map(int,input().split()))
listNumber=list(map(int,input().split()))
i=0
while i<Number[1]-1:
    i+=listNumber[i]
if i==(Number[1]-1):
    print("YES")
else:
    print("NO")


    
