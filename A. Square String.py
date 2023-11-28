for i in range(int(input())):
    str_input=input()
    other_str=len(str_input)//2
    rest_str=str_input[:other_str]
    new_str=str_input[-other_str:]
    if(len(str_input)%2==0 and (rest_str==new_str)):
        print("YES")
    else:
        print("NO")
