for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    b=''.join(map(str,s))
    zeros = [len(substr) for substr in b.split('1') if substr.count('0') == len(substr)]
    longest = max(zeros)
    print(longest)
