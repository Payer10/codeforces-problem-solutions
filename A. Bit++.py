n=int(input())
m=0
for i in range(n):
    i=input()
    if(i=="++X" or i=="X++"):
        m+=1
    elif(i=="--X" or i=="X--"):
        m-=1
print(m)
        
