for i in range(int(input())):
    number=int(input())
    string=input()
    count=0
    rest=0
    for a in range(number):
        if((a+1)==number):
            break
        if(string[a]=='1' and string[a+1]=='1'):
            count+=1
        if(string[a]=='0' and string[a+1]=='0'):
            rest+=1
    print(max(count,rest))
        
