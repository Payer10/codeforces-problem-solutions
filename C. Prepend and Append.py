for i in range(int(input())):
    Number=int(input())
    string=input()
    n=Number//2
    count=0
    for j in range(1,n+1):
        if(string[j-1]=='0' and string[Number-j]=='1'):
            count+=2
        elif(string[j-1]=='1' and string[Number-j]=='0'):
            count+=2
        else:
            break
    print(Number-count)
        
