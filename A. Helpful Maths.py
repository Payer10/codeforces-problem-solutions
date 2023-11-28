n=input().split("+")
n.sort()
output=""
for i in n:
    output+=i+"+"
print(output[:-1])
