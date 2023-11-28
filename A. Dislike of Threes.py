for i in range(int(input())):
    k=int(input())
    j=0
    a=1
    while(j<k):
        if(a%3!=0 and a%10!=3):           
            j+=1
        a+=1
    print(a-1)

