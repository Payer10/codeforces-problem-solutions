Digit=int(input())
for i in range(Digit):
    sumDigit=str(Digit+1)
    if(sumDigit[0]==sumDigit[1] or sumDigit[0]==sumDigit[2] or sumDigit[0]==sumDigit[3] or sumDigit[1]==sumDigit[2] or sumDigit[1]==sumDigit[3] or sumDigit[2]==sumDigit[3]):
        Digit+=1
    else:
        print(sumDigit)
        break
            
        
