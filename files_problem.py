f = open('Numbers', 'w+')
f.write('123321')
f.close()
f = open('Numbers', 'r+')
some_list = list(f.read())
f.close()
is_palindromic = True
for i in range(len(some_list)//2):
    if(some_list[i]!=some_list[len(some_list)-i-1]):
        is_palindromic = False
if is_palindromic:
    f = open('Numbers', 'a')
    f.write('Yes')
    f.close()
else:
    f = open('Numbers', 'w')
    f.write(len(some_list)*'0')
    
