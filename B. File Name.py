n = int(input())
s = input()
cnt = 0
ans = 0
for i in range(n):
    if s[i] == 'x':
        cnt += 1
    else:
        cnt = 0
            
    if cnt == 3:
        ans += 1
        cnt -= 1
print(ans)
