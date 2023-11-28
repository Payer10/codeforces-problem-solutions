def Polycrap_and_the_day_of_pi(s):
    n='314159265358979323846264338327'
    c=0
    for i in range(len(s)):
        if(n[c]==s[c]):
            c+=1
    return c
for i in range(int(input())):
    s=input()
    print(Polycrap_and_the_day_of_pi(s))
