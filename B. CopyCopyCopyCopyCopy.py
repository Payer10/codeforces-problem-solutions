for i in range(int(input())):
    Number=int(input())
    count=1
    listdi=list(map(int,input().split()))
    newli=sorted(listdi)
    for j in range(Number):
        if((j+1)==Number):
            break
        if(newli[j]==newli[j+1]):
            count+=0
        else:
            count+=1
    print(count)
