def solved(a,b):
    if(b==0):
        return a
    return solved(b,a%b)
if __name__ =="__main__":
    for i in range(int(input())):
        a,b=map(int,input().split())
        print(solved(a,b))
