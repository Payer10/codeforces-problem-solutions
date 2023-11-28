testcase=int(input())
for i in range(testcase):
    Number=int(input())
    newNum=Number//3
    Numnew=Number//3
    if(Number%3==1):
        newNum+=1
        print(newNum,Numnew)
    elif(Number%3==2):
        Numnew+=1
        print(newNum,Numnew)
    else:
        print(newNum,Numnew)
