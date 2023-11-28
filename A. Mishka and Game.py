miska1=0
chris1=0
for i in range(int(input())):
    miska,chris=map(int,input().split())
    if(miska>chris):
        miska1+=1
    elif(miska==chris):
        miska1+=0
        chris1+=0
    else:
        chris1+=1

if(miska1>chris1):
    print('Mishka')
elif(miska1==chris1):
    print('Friendship is magic!^^')
else:
    print('Chris')
