n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a%b==0):
        print('0')
    if(b<a and a%b!=0):
        restN=a//b
        Num=(restN+1)*b
        print(Num-a)
    elif(a<b):
        print(b-a)
