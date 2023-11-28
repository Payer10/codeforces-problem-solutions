for i in range(int(input())):
    Number=int(input())
    if(Number==2):
        print(1,2)
    elif(Number%2==1):
        print(-1)
    else:
        count=0
        newli=[]
        for a in range(1,Number+1):
            count+=a
            if(a%2==1):
                a+=1
            elif(a%2==0):
                a-=1
            newli.append(a)
        b=Number - len(str(Number)) + 1
        print(*newli)
            
