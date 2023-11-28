listsum=[]
for i in range(int(input())):
    string=input()
    listsum.append(string)
newlist=[]
restlist=[]
for j in range(len(listsum)):
    e=listsum[0]
    if(e == listsum[j]):
        newlist.append(listsum[j])
    else:
        restlist.append(listsum[j])
if(len(newlist)>=len(restlist)):
    print(newlist[0])
else:
    print(restlist[0])
