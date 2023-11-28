n=int(input())
s=input().split()[1:]
t=input().split()[1:]
if(len(set(s+t)) == n):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
