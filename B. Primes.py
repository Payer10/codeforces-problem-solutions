import math
def prime(n):
    for i in range(2,int(math.sqrt(n))):
        if(n%i==0):
            return False
    return True
if __name__ =="__main__":
    li=[]
    n=int(input())
    for i in range(2,n):
        if(prime(i)==int(i)):
            li.append(i)
    if(sum(li)==n):
        print(*li)
    else:
        print("-1")
    print(li)      
        
