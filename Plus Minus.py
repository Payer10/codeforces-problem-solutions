l=list(map(int,input().split()))
zero=0
plus=0
minus=0
for i in l:
    if i==0:
        zero+=1
    if i<0:
        minus+=1
    if i>0:
        plus+=1
z=zero/len(l)
p=plus/len(l)
m=minus/len(l)
print('%.6f'%p)
print('%.6f'%m)
print('%.6f'%z)
