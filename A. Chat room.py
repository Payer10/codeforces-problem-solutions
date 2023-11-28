m="hello"
def chatroom(s):
    x=0
    for i in range(len(s)):
        if(s[i]==m[x]):
            x+=1
        if(x==5):
            return "YES"
    return "NO"
if __name__ =="__main__":
    s=input()
    print(chatroom(s))
