number=int(input())
listNumber=list(map(int,input().split()))
sortedlist=sorted(listNumber)[:-1]
lists=[]
count=0
#print(sortedlist)
for i in range(number):
    #print(sortedlist)
    if(i==len(sortedlist)):
        break
    else:
        restsum=sum(listNumber)-sortedlist[i]
        lists.append(sortedlist[i])
        sortedlist.remove(sortedlist[i])
        if(restsum!<max(sortedlist)):
            count=1
            break
        else:
            count+=1
print(count)
    
    
    
    
    
    
