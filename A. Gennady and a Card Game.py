string=input()
list_str=list(map(str,input().split()))
new_str=""
for i in range(len(list_str)):
    new_str+=list_str[i]
if(string[0] in new_str or string[1] in new_str):
    print('YES')
else:
    print('NO')
