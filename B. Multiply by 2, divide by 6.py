for i in range(int(input())):
    Number=int(input())
    count=0
    while(Number!=1):
        if(Number%6==0):
            Number/=6
            count+=1
        elif(Number%3==0):
            Number*=2
            count+=1
        else:
            count=-1
            break
    print(count)
