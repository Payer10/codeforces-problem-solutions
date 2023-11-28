for _ in range(int(input())):
	n, m = map(int, input().split())
	c = [''] * m
	for i in range(n):
		s = input()
		for i in range(len(s)):
			c[i] += s[i]
	a = 'vika'
	i = 0
	for b in a:
		while i < m:
			if b in c[i]:
				i += 1
				break
			i += 1
		else:
			print("NO")
			break
	else:
		print("YES")