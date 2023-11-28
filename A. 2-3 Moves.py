for i in range(int(input())):
    N=int(input())
    if(N<2):
        print('2')
    if(N%3==0):
        print(N//3)
    elif(N%3==2):
        n=N+1
        print(n//3)
    elif(N>2 and N%3==1):
        n=N+2
        print(n//3)
