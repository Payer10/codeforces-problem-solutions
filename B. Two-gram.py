N=int(input())
s=input()
li=[]
a=''
if(len(s)==2):
    print(s)
else:
    for i in range(len(s)):
        if((i+1)==N):
            break
        if(s[i] not in li and s[i+1] not in li):
            li.append(s[i])
            li.append(s[i+1])
        elif(s[i] in li and s[i+1] in li):
            a+=s[i]
            a+=s[i+1]
            break
    print("{}{}".format(li[0],li[1]))
