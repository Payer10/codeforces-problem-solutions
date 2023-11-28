def min_operations_to_substring(x, s):
    operations = 0
    while s not in x:
        x += x
        operations += 1
    return operations

# Read input
for i in range(int(input())):
    a,b=map(int,input().split())
    x = input()
    s = input()

    # Find the minimum number of operations
    operations = min_operations_to_substring(x, s)
    print(operations)
