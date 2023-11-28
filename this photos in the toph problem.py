#iiiiiieeeeaaaiiiiooopp
s=input()
a=''
for i in range(len(s)):
    if(s[i]!=s[i-1]):
        a+=s[i]
print(a)
print(len(a)*5)
