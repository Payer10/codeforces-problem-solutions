s=input().lower()
a='a','e','i','o','u','y'
l=''
for i in range(0,len(s)):
    if s[i] not in a:
        l+='.'
        l+=s[i]
print(l)
    

