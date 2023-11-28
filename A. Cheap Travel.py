nNum,mNum,aNum,bNum=map(int,input().split())
if(mNum*aNum <= bNum):
    print(nNum*aNum)
else:
    sumNum = (nNum//mNum)*bNum+min((nNum%mNum)*aNum,bNum)
    print(sumNum)
                        
