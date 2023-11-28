n=int(input())
s=input()
n=0
m=0
for i in s:
    if(i=="D"):
        n+=1
    elif(i=="A"):
        m+=1
if(n==m):
    print("Friendship")
elif(n>m):
    print("Danik")
else:
    print("Anton")

