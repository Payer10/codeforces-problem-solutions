Num=int(input())
li_Num=list(map(int,input().split()))
new_li1=[]
new_li2=[]
new_li3=[]
for i in range(len(li_Num)):
    if(li_Num[i]==1):
        new_li1.append(i+1)
    elif(li_Num[i]==2):
        new_li2.append(i+1)
    elif(li_Num[i]==3):
        new_li3.append(i+1)
if(len(new_li1)==0 or len(new_li2)==0 or len(new_li3)==0):
    print('0')
else:
    a=len(new_li1)
    b=len(new_li2)
    c=len(new_li3)
    min_li=min(a,b,c)
    print(min_li)
    for i in range(min_li+1):
        if(i==min_li):
            break
        else:
            print('{} {} {}'.format(new_li1[i],new_li2[i],new_li3[i]))
        
