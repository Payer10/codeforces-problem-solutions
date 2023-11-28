for i in range(int(input())):
    a,b=map(int,input().split())
    c=(b-1).bit_length()
    print(c-(2**c-a)//b)
   